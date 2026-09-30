items = []

print("Shopping List")

while True:
    print("\n1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Clear list")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("What do you want to add? ")
        items.append(item)
        print(f"{item} added! 🛒")
   
    elif choice == "2":
        if len(items) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nShopping List:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]}")

    elif choice == "3":
        if len(items) == 0:
            print("Your shopping list is empty.")
        else:
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]}")

            number = int(input("Which item do you want to remove? "))

            if 1 <= number <= len(items):
                removed = items.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid item number.")

    elif choice == "4":
        items.clear()
        print("Shopping list cleared!")

    elif choice == "5":
        print("Happy shopping! 🛍️")
        break

    else:
        print("Please choose a number from 1 to 5.")