import random

choices = ["rock", "paper", "scissors"]

print("Rock Paper Scissors")

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win! 🎉")

    else:
        print("You lose!")

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break