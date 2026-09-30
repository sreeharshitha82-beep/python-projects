print("Tip Calculator")

while True:
    bill = float(input("What's the total bill? ₹"))
    tip = float(input("What tip percentage do you want to give? "))
    people = int(input("How many people are splitting the bill? "))

    tip_amount = bill * tip / 100
    total = bill + tip_amount
    each = total / people

    print()
    print(f"Bill: ₹{bill:.2f}")
    print(f"Tip: ₹{tip_amount:.2f}")
    print(f"Total: ₹{total:.2f}")
    print(f"Each person pays: ₹{each:.2f}")

    again = input("\nCalculate another bill? (y/n): ").lower()

    if again != "y":
        print("Bye!")
        break