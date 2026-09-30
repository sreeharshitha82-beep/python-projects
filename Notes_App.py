
import json
import os
from datetime import datetime

file = "notes.json"


def load_notes():
    if os.path.exists(file):
        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Could not load notes. Starting with an empty list.")
    return []


def save_notes():
    with open(file, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)


def show_notes(items):
    if not items:
        print("No notes found.")
        return

    for i, note in enumerate(items, start=1):
        pin = "📌 " if note["pinned"] else ""
        print(f"\n{i}. {pin}{note['title']}")
        print("Category:", note["category"])
        print("Created:", note["created"])
        print(note["content"])


def add_note():
    title = input("Title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    content = input("Content: ").strip()
    category = input("Category: ").strip() or "General"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    note = {
        "title": title,
        "content": content,
        "category": category,
        "pinned": False,
        "created": now,
        "updated": now
    }

    notes.append(note)
    save_notes()
    print("Note saved! 📝")


def edit_note():
    show_notes(notes)

    if not notes:
        return

    number = input("\nWhich note do you want to edit? ")

    if not number.isdecimal() or not 1 <= int(number) <= len(notes):
        print("Invalid note number.")
        return

    note = notes[int(number) - 1]

    title = input(f"New title [{note['title']}]: ").strip()
    content = input("New content (leave blank to keep): ").strip()
    category = input(f"New category [{note['category']}]: ").strip()

    if title:
        note["title"] = title

    if content:
        note["content"] = content

    if category:
        note["category"] = category

    note["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    save_notes()
    print("Note updated! ✏️")


def delete_note():
    show_notes(notes)

    if not notes:
        return

    number = input("\nWhich note do you want to delete? ")

    if not number.isdecimal() or not 1 <= int(number) <= len(notes):
        print("Invalid note number.")
        return

    note = notes.pop(int(number) - 1)
    save_notes()
    print(f"Deleted: {note['title']}")


def search_notes():
    search = input("Search: ").strip().lower()

    if not search:
        print("Enter something to search.")
        return

    found = [
        note for note in notes
        if search in note["title"].lower()
        or search in note["content"].lower()
        or search in note["category"].lower()
    ]

    show_notes(found)


def pin_note():
    show_notes(notes)

    if not notes:
        return

    number = input("\nWhich note do you want to pin or unpin? ")

    if not number.isdecimal() or not 1 <= int(number) <= len(notes):
        print("Invalid note number.")
        return

    note = notes[int(number) - 1]
    note["pinned"] = not note["pinned"]

    save_notes()

    if note["pinned"]:
        print("Note pinned! 📌")
    else:
        print("Note unpinned.")


def show_categories():
    categories = sorted(set(note["category"] for note in notes))

    if not categories:
        print("No categories found.")
        return

    print("\nCategories:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    choice = input("Choose a category: ")

    if not choice.isdecimal() or not 1 <= int(choice) <= len(categories):
        print("Invalid category.")
        return

    category = categories[int(choice) - 1]

    found = [note for note in notes if note["category"] == category]
    show_notes(found)


notes = load_notes()

while True:
    notes.sort(key=lambda note: note["pinned"], reverse=True)

    print("\n" + "=" * 30)
    print("          NOTES APP")
    print("=" * 30)

    print("1. Add note")
    print("2. View notes")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Search notes")
    print("6. Pin or unpin note")
    print("7. View categories")
    print("8. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes(notes)
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        search_notes()
    elif choice == "6":
        pin_note()
    elif choice == "7":
        show_categories()
    elif choice == "8":
        print("Your notes are saved. Goodbye! 👋")
        break
    else:
        print("Please choose a number from 1 to 8.")