tasks = []

print("To-Do List")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added! ✅")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your list is empty.")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Your list is empty.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Which task do you want to remove? "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")