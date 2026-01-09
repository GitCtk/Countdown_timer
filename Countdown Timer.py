# Countdown Timer
# Author: Kenan Kozlica

"""
Flowchart/Diagram for program:
+-------------------+
| Start program     |
+---------+---------+
          |
          v
+-------------------+
| Display instructions|
+---------+---------+
          |
          v
+-------------------+
| User input choice |
+---------+---------+
   |           |
   v           v
seconds?     date?
   |           |
   v           v
Enter seconds   Create empty list of targets
   |           |
Countdown      Input date/times into list or select file with date/times
   |           |
   |       Countdown for each target
   |           |
   +------+----+
          v
       Program ends
"""

import time
from datetime import datetime

def convert_to_dhms(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

def countdown_seconds(duration):
    while duration >= 0:
        d, h, m, s = convert_to_dhms(duration)
        print(f"\rTime remaining: D:%5d H:%2d M:%2d S:%2d" % (d,h,m,s), end="")
        time.sleep(1)
        duration -= 1
    print("\nTime is up!")

def countdown_to_date(target_list):
    ok = True
    print ("Countdown for: ")
    for idx, target_time in enumerate(target_list, 1):
        print(f"{target_time}      ", end="") 
    print (f"")     
    while ok:
        ok = False
        print (f"\r", end="")
        for idx, target_time in enumerate(target_list, 1):
            seconds = int((target_time - datetime.now()).total_seconds())
            if seconds > 0: 
                ok = True
                d, h, m, s = convert_to_dhms(seconds)
                print(f"D:%5d H:%2d M:%2d S:%2d   " % (d,h,m,s), end="")
            else:
                print(f"Time is up!              ", end="")
        if not ok: break 
        time.sleep(1)
   
def main_program():
    print("=== Countdown Calculator ===")
    choice = input("Seconds or date? (seconds/date): ").strip().lower()
    if choice == "seconds":
        while True:
            try:
                duration = int(input("Enter number of seconds: "))
                if duration < 0: 
                    print("Target time is in the past! Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number.")
        countdown_seconds(duration)
    elif choice == "date":
        target_list = []
        while True:
            entry = input("Enter target date/time (YYYY-MM-DD HH:MM:SS) or file:<> or 'end': ")
            if entry.lower()[:5] == "file:":
                filename = entry.lower()[5:]
                try:
                    with open (filename, 'r') as file:
                        line = file.readline ().strip()
                        while line:
                            try:
                                target_time = datetime.strptime(line, "%Y-%m-%d %H:%M:%S")
                                if target_time <= datetime.now(): 
                                    print("Read form file: Target time is in the past")
                                    line = file.readline ().strip()
                                    continue
                                target_list.append(target_time)
                            except ValueError:
                                print("Read from file: Incorrect format.")
                            line = file.readline ().strip()
                except IOError:
                    print("Error! Could not open file")          
                continue
            if entry.lower() == "end": break
            try:
                target_time = datetime.strptime(entry, "%Y-%m-%d %H:%M:%S")
                if target_time <= datetime.now(): 
                    print("Target time is in the past")
                    continue
                target_list.append(target_time)
            except ValueError:
                print("Incorrect format.")
        countdown_to_date(target_list)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_program()
