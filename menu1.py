from datetime import datetime
from menu import menu
import schedule
import time

print('Versiunea 6')

def start_scheduled_task(start_date, interval):
    current_time = datetime.now()
    if current_time >= start_date:
        menu()

        while datetime.now() > start_date:
            schedule.every(interval).seconds.do(menu)
            schedule.run_pending()
            time.sleep(1)
    else:
       
        while current_time > start_date:
            time.sleep(1)
            current_time = datetime.now()
        menu()


start_date = datetime(2024, 12, 1)
start_scheduled_task(start_date, 5)
