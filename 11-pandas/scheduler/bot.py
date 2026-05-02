"""
bot.py — Selenium automation: logs in and clicks a target button.
Configure the constants below before running.
"""

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
)

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

LOGIN_URL       = "https://example.com/login"       # URL of the login page
TARGET_URL      = "https://example.com/dashboard"   # URL where the button lives (leave "" to stay on same page after login)

USERNAME        = "your_username"
PASSWORD        = "your_password"

# Selectors for the login form — change By.ID / By.NAME / By.XPATH etc. as needed
USERNAME_SELECTOR = (By.ID, "username")
PASSWORD_SELECTOR = (By.ID, "password")
SUBMIT_SELECTOR   = (By.XPATH, '//button[@type="submit"]')

# Selector for the button to click after login
TARGET_BUTTON_SELECTOR = (By.XPATH, '//button[contains(text(), "Click Me")]')

# How long (seconds) to wait for elements before timing out
WAIT_TIMEOUT = 15

# Run headlessly? Set True for server / cron use; False to watch the browser
HEADLESS = True

# ─── LOGGING ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ─── DRIVER SETUP ─────────────────────────────────────────────────────────────

def build_driver() -> webdriver.Chrome:
    opts = Options()
    if HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    # Suppress "Chrome is being controlled by automated software" bar
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(5)
    return driver


# ─── CORE LOGIC ───────────────────────────────────────────────────────────────

def login(driver: webdriver.Chrome, wait: WebDriverWait) -> None:
    log.info("Navigating to login page: %s", LOGIN_URL)
    driver.get(LOGIN_URL)

    log.info("Entering credentials …")
    wait.until(EC.visibility_of_element_located(USERNAME_SELECTOR)).send_keys(USERNAME)
    driver.find_element(*PASSWORD_SELECTOR).send_keys(PASSWORD)
    driver.find_element(*SUBMIT_SELECTOR).click()

    # Wait until the URL changes away from the login page as a simple success check
    wait.until(EC.url_changes(LOGIN_URL))
    log.info("Login successful — now at: %s", driver.current_url)


def click_target_button(driver: webdriver.Chrome, wait: WebDriverWait) -> None:
    if TARGET_URL:
        log.info("Navigating to target page: %s", TARGET_URL)
        driver.get(TARGET_URL)

    log.info("Waiting for target button …")
    btn = wait.until(EC.element_to_be_clickable(TARGET_BUTTON_SELECTOR))
    log.info("Clicking button: %s", btn.text or str(TARGET_BUTTON_SELECTOR))
    btn.click()
    log.info("Button clicked successfully.")


def run() -> None:
    driver = None
    try:
        driver = build_driver()
        wait   = WebDriverWait(driver, WAIT_TIMEOUT)

        login(driver, wait)
        click_target_button(driver, wait)

        # Small pause so any post-click action can settle
        time.sleep(2)
        log.info("Task completed successfully.")

    except TimeoutException as exc:
        log.error("Timed out waiting for an element: %s", exc.msg)
    except NoSuchElementException as exc:
        log.error("Element not found: %s", exc.msg)
    except WebDriverException as exc:
        log.error("WebDriver error: %s", exc.msg)
    except Exception as exc:  # noqa: BLE001
        log.exception("Unexpected error: %s", exc)
    finally:
        if driver:
            driver.quit()
            log.info("Browser closed.")


# ─── ENTRY POINT ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run()
