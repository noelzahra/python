# Selenium Cron Bot

Logs into a website and clicks a button automatically at a scheduled time.

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

You also need **Google Chrome** installed, plus `chromedriver` matching your Chrome version.
The easiest way is to let `webdriver-manager` handle it automatically — replace the driver
line in `bot.py` with:

```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts,
)
```

---

## 2. Configure bot.py

Open `bot.py` and fill in the constants at the top:

| Constant | What to set |
|---|---|
| `LOGIN_URL` | Full URL of the login page |
| `TARGET_URL` | URL where the button lives (empty string = stay on page after login) |
| `USERNAME` / `PASSWORD` | Your credentials |
| `USERNAME_SELECTOR` | Selenium locator for the username field |
| `PASSWORD_SELECTOR` | Selenium locator for the password field |
| `SUBMIT_SELECTOR` | Selenium locator for the login submit button |
| `TARGET_BUTTON_SELECTOR` | Selenium locator for the button to click |
| `HEADLESS` | `True` for servers, `False` to watch the browser |

### Finding selectors

Open DevTools in Chrome (F12), right-click the element → **Inspect**, then right-click
the highlighted HTML → **Copy → Copy XPath** (or use `By.ID`, `By.NAME`, `By.CSS_SELECTOR`).

---

## 3. Test a single run

```bash
python bot.py
# or
python scheduler.py --now
```

---

## 4. Schedule — Option A: Python scheduler (cross-platform)

Set `RUN_AT = "HH:MM"` in `scheduler.py`, then run it as a persistent process:

```bash
python scheduler.py
```

To keep it running after you log out, use `nohup` or `screen`:

```bash
nohup python scheduler.py &
```

---

## 5. Schedule — Option B: System cron (Linux/macOS)

```bash
crontab -e
```

Add a line — example for every day at 08:00:

```
0 8 * * * /usr/bin/python3 /path/to/selenium_cron/bot.py >> /path/to/selenium_cron/bot.log 2>&1
```

Cron format:
```
┌──────── minute  (0-59)
│ ┌─────── hour    (0-23)
│ │ ┌────── day of month (1-31)
│ │ │ ┌───── month  (1-12)
│ │ │ │ ┌──── day of week (0-7, 0=Sun)
│ │ │ │ │
* * * * *  command
```

Common schedules:

| Schedule | Cron expression |
|---|---|
| Every day at 08:00 | `0 8 * * *` |
| Every day at 23:30 | `30 23 * * *` |
| Every weekday at 09:00 | `0 9 * * 1-5` |
| Every hour | `0 * * * *` |

> **Tip:** On Linux servers, Chrome must be installed and `DISPLAY` may need to be set
> if not running headless. The `--headless=new` flag in `bot.py` handles this automatically.

---

## Logs

- `bot.log` — individual run logs (login result, button click result, errors)
- `scheduler.log` — scheduler heartbeat and trigger events
