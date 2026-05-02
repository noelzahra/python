"""
scheduler.py — Runs bot.py at a fixed time every day using the `schedule` library.
Useful when you can't edit system crontab (e.g. inside a venv or container).

Usage:
    python scheduler.py          # keeps running; triggers bot at RUN_AT each day
    python scheduler.py --now    # run once immediately (good for testing)
"""

import argparse
import logging
import time

import schedule

from bot import run  # import the task from bot.py

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

# Time to run every day — 24-hour format "HH:MM"
RUN_AT = "08:00"

# ─── LOGGING ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    handlers=[
        logging.FileHandler("scheduler.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Scheduled Selenium bot")
    parser.add_argument(
        "--now", action="store_true", help="Run the bot immediately and exit"
    )
    args = parser.parse_args()

    if args.now:
        log.info("Running bot immediately (--now flag).")
        run()
        return

    log.info("Scheduler started — bot will run every day at %s.", RUN_AT)
    schedule.every().day.at(RUN_AT).do(run)

    while True:
        schedule.run_pending()
        time.sleep(30)  # check every 30 seconds


if __name__ == "__main__":
    main()
