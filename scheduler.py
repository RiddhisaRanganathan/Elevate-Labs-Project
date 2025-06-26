# Final scheduler.py

# scheduler.py
import schedule
import time
from alerter import monitor

def run_alert():
    print("[*] Running scheduled anomaly check...")
    monitor()

# Change the time interval here
schedule.every(2).minutes.do(run_alert)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] Scheduler stopped by user.")
