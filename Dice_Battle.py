import random

print("Dice Battle")
print("First to win 5 rounds wins the game!\n")

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    input("Press Enter to roll the dice...")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("\nYou rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        print("You win this round! 🎉")
        player_score += 1
    elif computer > player:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    print(f"Score: You {player_score} - Computer {computer_score}\n")

if player_score == 5:
    print("You won the battle! 🏆")
else:
    print("Computer won the battle! 🎲")
