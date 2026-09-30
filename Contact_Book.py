import json
import os

file = "contacts.json"


def load_contacts():
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_contacts():
    with open(file, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts()
    print("Contact saved! ✅")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")


def search_contact():
    search = input("Search name: ").lower()

    found = False

    for name, details in contacts.items():
        if search in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            found = True

    if not found:
        print("No matching contacts.")


def update_contact():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("New phone: ").strip()
    email = input("New email: ").strip()

    if phone:
        contacts[name]["phone"] = phone

    if email:
        contacts[name]["email"] = email

    save_contacts()
    print("Contact updated! ✏️")


def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted.")
    else:
        print("Contact not found.")


contacts = load_contacts()

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")

print("Contacts saved. Goodbye! 👋")