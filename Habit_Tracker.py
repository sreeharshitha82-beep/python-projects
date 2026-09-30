import json
import os
from datetime import date, timedelta

file = "habits.json"


def load_habits():
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_habits():
    with open(file, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=4)


def add_habit():
    name = input("Enter a habit: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    if name in habits:
        print("This habit already exists.")
        return

    habits[name] = {
        "completed": []
    }

    save_habits()
    print("Habit added! 🌱")


def view_habits():
    if not habits:
        print("No habits added yet.")
        return

    today = date.today().isoformat()

    print("\n--- YOUR HABITS ---")

    for i, (name, details) in enumerate(habits.items(), start=1):
        status = "✅ Done" if today in details["completed"] else "⬜ Not done"
        streak = get_streak(details["completed"])

        print(f"{i}. {name}")
        print(f"   Status: {status}")
        print(f"   Current streak: {streak} days")


def mark_completed():
    view_habits()

    if not habits:
        return

    name = input("\nEnter habit name to mark complete: ").strip()

    if name not in habits:
        print("Habit not found.")
        return

    today = date.today().isoformat()
    completed = habits[name]["completed"]

    if today in completed:
        print("Already completed today! 🎉")
    else:
        completed.append(today)
        save_habits()
        print("Habit completed! 🎉")


def get_streak(completed):
    completed_dates = set(completed)
    today = date.today()

    if today.isoformat() not in completed_dates:
        today -= timedelta(days=1)

    streak = 0

    while today.isoformat() in completed_dates:
        streak += 1
        today -= timedelta(days=1)

    return streak


def view_history():
    view_habits()

    if not habits:
        return

    name = input("\nEnter habit name to view history: ").strip()

    if name not in habits:
        print("Habit not found.")
        return

    completed = sorted(habits[name]["completed"], reverse=True)

    print(f"\n--- HISTORY: {name} ---")

    if not completed:
        print("No completed days yet.")
    else:
        for day in completed:
            print(f"✅ {day}")


def delete_habit():
    view_habits()

    if not habits:
        return

    name = input("\nEnter habit name to delete: ").strip()

    if name in habits:
        del habits[name]
        save_habits()
        print("Habit deleted.")
    else:
        print("Habit not found.")


habits = load_habits()

while True:
    print("\n" + "=" * 30)
    print("       HABIT TRACKER")
    print("=" * 30)

    print("1. Add habit")
    print("2. View habits")
    print("3. Mark habit completed")
    print("4. View history")
    print("5. Delete habit")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        view_habits()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        view_history()
    elif choice == "5":
        delete_habit()
    elif choice == "6":
        print("Progress saved. Keep going! 🌱")
        break
    else:
        print("Invalid choice.")