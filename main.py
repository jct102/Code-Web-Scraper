import schedule
import time
from text import send_text

# Every day at 10am send a text with the updated codes
schedule.every().day.at("10:00").do(send_text())

while True:
    schedule.run_pending()
    time.sleep(1)
