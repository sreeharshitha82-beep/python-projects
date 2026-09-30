import random
import time


def intro():
    print('''You are in a land full of dragons.

There are two caves in front of you.
One dragon is friendly and will share its treasure.
The other is hungry and will eat you.''')
    print()


def choose_cave():
    while True:
        cave = input("Which cave will you enter? (1 or 2): ")

        if cave in ('1', '2'):
            return cave

        print("Please choose cave 1 or 2.")


def check_cave(cave):
    print("You walk towards the cave...")
    time.sleep(2)

    print("It's dark and spooky...")
    time.sleep(2)

    print("A huge dragon jumps out!")
    print("It opens its jaws and...")
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if cave == str(friendly_cave):
        print("The dragon gives you its treasure! 🐉💰")
    else:
        print("The dragon gobbles you up! 💀")


while True:
    intro()

    cave = choose_cave()
    check_cave(cave)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again not in ('yes', 'y'):
        print("Thanks for playing!")
        break