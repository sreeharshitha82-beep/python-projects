import random

print("Higher or Lower")
print("Guess if the next number will be higher or lower.")

score = 0
number = random.randint(1, 100)

while True:
    print("\nCurrent number:", number)

    choice = input("Higher or lower? (h/l): ").lower()

    if choice != "h" and choice != "l":
        print("Please enter h or l.")
        continue

    next_number = random.randint(1, 100)

    print("Next number:", next_number)

    if next_number == number:
        print("Same number! No points.")
    elif choice == "h" and next_number > number:
        print("Correct! 🎉")
        score += 1
    elif choice == "l" and next_number < number:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong! Game over.")
        break

    print("Score:", score)
    number = next_number

print("\nFinal score:", score)
