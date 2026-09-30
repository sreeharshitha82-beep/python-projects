import random
import string


def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    else:
        return "Strong"


while True:
    print("\n" + "=" * 30)
    print("     PASSWORD GENERATOR")
    print("=" * 30)

    print("1. Generate password")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            length = int(input("Password length: "))

            if length < 1:
                print("Length must be at least 1.")
                continue

            use_digits = input("Include numbers? (y/n): ").lower() == "y"
            use_symbols = input("Include symbols? (y/n): ").lower() == "y"

            password = generate_password(
                length,
                use_digits,
                use_symbols
            )

            print("\nYour password:", password)
            print("Strength:", check_strength(password))

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        print("Goodbye! 🔒")
        break

    else:
        print("Invalid choice.")