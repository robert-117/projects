from datetime import datetime
import sys
import time

print("Counting down the time until the new year")
print("-----------------------------------------")

while True:

    now = datetime.now()
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1, 0, 0, 0)

    delta = new_year - now

    days = delta.days
    seconds = delta.seconds % 60
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60


    line = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    # sys.stdout.write("\033c")
    time.sleep(1)
    sys.stdout.write("\r" + line)
    sys.stdout.flush()
    if delta.seconds == 0:
        break
    else:
        continue

print("\nhappy new year!")