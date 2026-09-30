print("Unit Converter")

while True:
    print("\n1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "2":
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles = {km:.2f} km")

    elif choice == "3":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} pounds")

    elif choice == "4":
        pounds = float(input("Enter pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds = {kg:.2f} kg")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Please choose a number from 1 to 5.")
        