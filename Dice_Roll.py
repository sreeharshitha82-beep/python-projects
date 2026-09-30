import random

print("Dice Roller")

while True:
    dice = int(input("How many dice do you want to roll? "))

    total = 0

    for i in range(dice):
        roll = random.randint(1, 6)
        print("You rolled:", roll)
        total += roll

    print("Total:", total)

    again = input("Roll again? (y/n): ").lower()

    if again != "y":
        print("Bye!")
        break