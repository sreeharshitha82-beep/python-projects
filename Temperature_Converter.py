print("Temperature Converter")

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print(f"{c}°C is {f:.1f}°F")

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print(f"{f}°F is {c:.1f}°C")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Please choose 1, 2, or 3.")