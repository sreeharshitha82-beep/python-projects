import random

print("Fortune Cookie")
print("Let's see what your fortune is...\n")

fortunes = [
    "Good things are coming your way. 🍀",
    "You will learn something new today.",
    "Someone will make you laugh soon.",
    "Your hard work will pay off.",
    "A surprise is waiting for you.",
    "You should trust yourself more.",
    "Today is a good day to try something new.",
    "Your future looks suspiciously productive. 😌",
    "You will find exactly what you are looking for.",
    "You are going to have a lucky day!"
]

while True:
    input("Press Enter to crack the cookie...")

    print("\n🥠 Your fortune:")
    print(random.choice(fortunes))

    again = input("\nWant another fortune? (y/n): ").lower()

    if again != "y":
        print("Your fortune has been sealed. Goodbye! 🥠")
        break