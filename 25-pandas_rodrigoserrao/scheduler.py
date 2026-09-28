"""
scheduler.py — Runs pandas_rodrigos.py at a fixed time every day using the `schedule` library.
Useful when you can't edit system crontab / Task Scheduler (e.g. inside a venv or container).

Usage:
    python scheduler.py          # keeps running; triggers the script at RUN_AT each day
    python scheduler.py --now    # run once immediately (good for testing)
"""

import argparse
import logging
import time

import schedule

from pandas_rodrigos import main as run

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

# Time to run every day — 24-hour format "HH:MM"
RUN_AT = "07:15"

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
    parser = argparse.ArgumentParser(description="Scheduled pandas_rodrigos runner")
    parser.add_argument(
        "--now", action="store_true", help="Run the script immediately and exit"
    )
    args = parser.parse_args()

    if args.now:
        log.info("Running pandas_rodrigos immediately (--now flag).")
        run()
        return

    log.info("Scheduler started — pandas_rodrigos will run every day at %s.", RUN_AT)
    schedule.every().day.at(RUN_AT).do(run)

    while True:
        schedule.run_pending()
        time.sleep(30)  # check every 30 seconds


if __name__ == "__main__":
    main()
