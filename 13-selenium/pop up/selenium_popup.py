from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
    NoSuchElementException,
)


def click_button_and_get_popup_message(
    driver: webdriver.Remote,
    button_locator: tuple,
    popup_type: str = "alert",
    popup_locator: tuple = None,
    timeout: int = 10,
) -> str:
    """
    Clicks a button and returns the text from the resulting popup message.

    Args:
        driver:          Selenium WebDriver instance.
        button_locator:  Tuple of (By.X, "selector") identifying the button,
                         e.g. (By.ID, "run-daybatch").
        popup_type:      One of:
                           "alert"   – native browser alert/confirm/prompt
                           "element" – in-page element (toast, modal, banner)
        popup_locator:   Required when popup_type="element".
                         Tuple of (By.X, "selector") for the popup element.
        timeout:         Seconds to wait for the popup to appear.

    Returns:
        The popup message string, e.g. "Daybatch complete".

    Raises:
        ValueError:        Unknown popup_type or missing popup_locator.
        TimeoutException:  Popup did not appear within `timeout` seconds.
        NoAlertPresentException: Expected alert was not raised.
    """
    if popup_type not in ("alert", "element"):
        raise ValueError(f"popup_type must be 'alert' or 'element', got '{popup_type}'")

    if popup_type == "element" and popup_locator is None:
        raise ValueError("popup_locator is required when popup_type='element'")

    # ── 1. Wait for the button and click it ──────────────────────────────────
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(button_locator),
        message=f"Button not clickable: {button_locator}",
    )
    button.click()

    # ── 2. Capture the popup message ─────────────────────────────────────────
    if popup_type == "alert":
        return _get_alert_message(driver, timeout)
    else:
        return _get_element_message(driver, popup_locator, timeout)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get_alert_message(driver: webdriver.Remote, timeout: int) -> str:
    """Handles a native browser alert and returns its text."""
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        alert.accept()          # dismiss the alert so execution can continue
        return message
    except TimeoutException:
        raise TimeoutException(f"No alert appeared within {timeout}s.")
    except NoAlertPresentException:
        raise NoAlertPresentException("Expected an alert but none was present.")


def _get_element_message(
    driver: webdriver.Remote,
    popup_locator: tuple,
    timeout: int,
) -> str:
    """Waits for an in-page popup element and returns its visible text."""
    try:
        popup_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(popup_locator),
            message=f"Popup element not visible: {popup_locator}",
        )
        return popup_element.text.strip()
    except TimeoutException:
        raise TimeoutException(
            f"Popup element {popup_locator} did not appear within {timeout}s."
        )


# ── Usage examples ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")      # remove for visual debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://your-app-url.com")

        # ── Example A: native browser alert ──────────────────────────────────
        message = click_button_and_get_popup_message(
            driver=driver,
            button_locator=(By.ID, "run-daybatch-btn"),
            popup_type="alert",
            timeout=10,
        )
        print(f"Alert message: {message}")   # → "Daybatch complete"

        # ── Example B: in-page toast / modal ─────────────────────────────────
        message = click_button_and_get_popup_message(
            driver=driver,
            button_locator=(By.CSS_SELECTOR, "button.submit"),
            popup_type="element",
            popup_locator=(By.CLASS_NAME, "toast-message"),
            timeout=10,
        )
        print(f"Toast message: {message}")   # → "Daybatch complete"

    finally:
        driver.quit()
