class Calculator:

    def display(self):
        print("\n================ Welcome to the Calculator! ================")
        print("================== Available operations: ===================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Floor Division")
        print("6. Modulus")
        print("7. Exponentiation")
        print("8. Exit")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def floor_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform floor division by zero.")
        return a // b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus operation by zero.")
        return a % b

    def exponentiate(self, a, b):
        return a ** b


def main():

    calculator = Calculator()

    while True:

        calculator.display()

        choice = input("\nEnter your choice (1-8): ")

        if choice == "8":
            print("\nExiting the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nInvalid choice. Please enter a number from 1 to 8.")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == "1":
                result = calculator.add(a, b)

            elif choice == "2":
                result = calculator.subtract(a, b)

            elif choice == "3":
                result = calculator.multiply(a, b)

            elif choice == "4":
                result = calculator.divide(a, b)

            elif choice == "5":
                result = calculator.floor_divide(a, b)

            elif choice == "6":
                result = calculator.modulus(a, b)

            elif choice == "7":
                result = calculator.exponentiate(a, b)

            print(f"\nChoice entered: {choice}")
            print(f"Result: {result}")
        except ValueError as e :
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()