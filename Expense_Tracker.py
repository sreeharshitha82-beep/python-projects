import json


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.load_expenses()

    # -------------------------------
    # LOAD EXPENSES
    # -------------------------------

    def load_expenses(self):

        try:
            with open(self.filename, "r") as file:
                self.expenses = json.load(file)

        except FileNotFoundError:
            self.expenses = []

        except json.JSONDecodeError:
            print("Error: The expense file is corrupted.")
            self.expenses = []


    # -------------------------------
    # SAVE EXPENSES
    # -------------------------------

    def save_expenses(self):

        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)


    # -------------------------------
    # GENERATE UNIQUE ID
    # -------------------------------

    def generate_id(self):

        if not self.expenses:
            return 1

        return max(expense["id"] for expense in self.expenses) + 1


    # -------------------------------
    # ADD EXPENSE
    # -------------------------------

    def add_expense(self):

        name = input("Enter expense name: ").strip()

        if not name:
            print("Expense name cannot be empty.")
            return

        while True:

            try:
                amount = float(input("Enter amount: "))

                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")


        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return


        expense = {
            "id": self.generate_id(),
            "name": name,
            "amount": amount,
            "category": category
        }


        self.expenses.append(expense)

        self.save_expenses()

        print("\nExpense added successfully!")


    # -------------------------------
    # VIEW EXPENSES
    # -------------------------------

    def view_expenses(self):

        if not self.expenses:
            print("\nNo expenses recorded.")
            return


        print("\n========================================")
        print("              EXPENSES")
        print("========================================")


        for expense in self.expenses:

            print(
                f"ID: {expense['id']} | "
                f"Name: {expense['name']} | "
                f"Amount: ₹{expense['amount']:.2f} | "
                f"Category: {expense['category']}"
            )


    # -------------------------------
    # CALCULATE TOTAL
    # -------------------------------

    def calculate_total(self):

        if not self.expenses:
            print("\nNo expenses recorded.")
            return


        total = 0

        for expense in self.expenses:
            total += expense["amount"]


        print(f"\nTotal spending: ₹{total:.2f}")


    # -------------------------------
    # CATEGORY SUMMARY
    # -------------------------------

    def category_summary(self):

        if not self.expenses:
            print("\nNo expenses recorded.")
            return


        category_totals = {}


        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]


            if category in category_totals:
                category_totals[category] += amount

            else:
                category_totals[category] = amount


        print("\n========================================")
        print("          CATEGORY SPENDING")
        print("========================================")


        for category, total in category_totals.items():

            print(
                f"{category}: ₹{total:.2f}"
            )


    # -------------------------------
    # DELETE EXPENSE
    # -------------------------------

    def delete_expense(self):

        if not self.expenses:
            print("\nNo expenses to delete.")
            return


        self.view_expenses()


        try:

            expense_id = int(
                input("\nEnter the ID of the expense to delete: ")
            )


            for expense in self.expenses:

                if expense["id"] == expense_id:

                    self.expenses.remove(expense)

                    self.save_expenses()

                    print("\nExpense deleted successfully.")

                    return


            print("\nExpense ID not found.")


        except ValueError:

            print("\nPlease enter a valid ID.")


# -----------------------------------
# MENU
# -----------------------------------

def display_menu():

    print("\n========================================")
    print("           EXPENSE TRACKER")
    print("========================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Category Spending")
    print("5. Delete Expense")
    print("6. Exit")
    print("========================================")


# -----------------------------------
# MAIN
# -----------------------------------

def main():

    tracker = ExpenseTracker()


    while True:

        display_menu()


        try:

            choice = int(
                input("Enter your choice: ")
            )


            if choice == 1:

                tracker.add_expense()


            elif choice == 2:

                tracker.view_expenses()


            elif choice == 3:

                tracker.calculate_total()


            elif choice == 4:

                tracker.category_summary()


            elif choice == 5:

                tracker.delete_expense()


            elif choice == 6:

                print("\nExiting Expense Tracker. Goodbye!")

                break


            else:

                print(
                    "\nInvalid choice. "
                    "Please choose between 1 and 6."
                )


        except ValueError:

            print("\nPlease enter a valid number.")


        input("\nPress Enter to continue...")


# -----------------------------------
# PROGRAM ENTRY POINT
# -----------------------------------

if __name__ == "__main__":
    main()