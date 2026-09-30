import random

numbers = {
    1: "ICHI",
    2: "NI",
    3: "SAN",
    4: "SHI",
    5: "GO",
    6: "ROKU"
}

print("Cho-Han")
print("Guess if the two dice add up to an even or odd number.\n")

money = 5000

while money > 0:
    print(f"You have {money} mon.")
    print("How much do you want to bet? (or QUIT)")

    while True:
        bet = input("> ")

        if bet.upper() == "QUIT":
            print("Thanks for playing!")
            exit()

        if not bet.isdecimal():
            print("Please enter a number.")
            continue

        bet = int(bet)

        if bet > money:
            print("You don't have enough money.")
            continue

        break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("\nThe dealer shakes the dice...")
    print("The cup hits the floor.")
    print("\nCHO = even")
    print("HAN = odd")

    while True:
        choice = input("\nYour guess: ").upper()

        if choice == "CHO" or choice == "HAN":
            break

        print("Please enter CHO or HAN.")

    print("\nThe dealer reveals the dice!")
    print(numbers[dice1], "-", numbers[dice2])
    print(dice1, "-", dice2)

    total = dice1 + dice2

    if total % 2 == 0:
        answer = "CHO"
    else:
        answer = "HAN"

    if choice == answer:
        print("\nYou won! 🎉")
        money += bet
        fee = bet // 10
        money -= fee
        print(f"The house takes a {fee} mon fee.")
    else:
        print("\nYou lost!")
        money -= bet

    print()

print("You ran out of money! 💸")
print("Thanks for playing!")