import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def show_clock():
    print("\nDigital Clock")
    print("Press Ctrl + C to go back.\n")

    try:
        while True:
            now = datetime.now()
            date = now.strftime("%A, %d %B %Y")
            clock = now.strftime("%H:%M:%S")

            print("\r" + date + " | " + clock, end="", flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n")


def show_12_hour_clock():
    print("\nDigital Clock")
    print("Press Ctrl + C to go back.\n")

    try:
        while True:
            now = datetime.now()
            date = now.strftime("%A, %d %B %Y")
            clock = now.strftime("%I:%M:%S %p")

            print("\r" + date + " | " + clock, end="", flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n")


def set_alarm():
    alarm = input("\nEnter alarm time (HH:MM): ")

    print("Alarm set for", alarm)
    print("Waiting...")

    while True:
        now = datetime.now()
        current = now.strftime("%H:%M")

        if current == alarm:
            print("\n\n⏰ ALARM! ⏰")
            print("It's", current)
            break

        time.sleep(1)


def stopwatch():
    print("\nStopwatch")
    input("Press Enter to start...")

    start = time.time()

    print("Stopwatch started!")
    input("Press Enter to stop...")

    end = time.time()

    seconds = end - start

    print(f"\nTime: {seconds:.2f} seconds")


def countdown():
    print("\nCountdown Timer")

    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    total = minutes * 60 + seconds

    while total >= 0:
        mins = total // 60
        secs = total % 60

        print(f"\rTime left: {mins:02d}:{secs:02d}", end="", flush=True)

        time.sleep(1)
        total -= 1

    print("\n⏰ Time's up!")


def world_clock():
    cities = {
        "1": ("New York", "America/New_York"),
        "2": ("London", "Europe/London"),
        "3": ("Dubai", "Asia/Dubai"),
        "4": ("Mumbai", "Asia/Kolkata"),
        "5": ("Tokyo", "Asia/Tokyo"),
        "6": ("Sydney", "Australia/Sydney")
    }

    print("\nWorld Clock")

    for number, city in cities.items():
        name, zone = city
        now = datetime.now(ZoneInfo(zone))
        clock = now.strftime("%H:%M:%S")
        print(f"{number}. {name}: {clock}")


while True:
    print("\n" + "=" * 35)
    print("          DIGITAL CLOCK")
    print("=" * 35)

    print("1. 24-hour clock")
    print("2. 12-hour clock")
    print("3. Set alarm")
    print("4. Stopwatch")
    print("5. Countdown timer")
    print("6. World clock")
    print("7. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        show_clock()

    elif choice == "2":
        show_12_hour_clock()

    elif choice == "3":
        set_alarm()

    elif choice == "4":
        stopwatch()

    elif choice == "5":
        countdown()

    elif choice == "6":
        world_clock()

    elif choice == "7":
        print("Goodbye! 👋")
        break

    else:
        print("Please choose a number from 1 to 7.")