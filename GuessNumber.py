import random

print("Guess the Number")
name = input("What's your name? ")

number = random.randint(1, 20)

print(f"Hey {name}! I'm thinking of a number between 1 and 20.")

for attempt in range(1, 7):
    print(f"Guess #{attempt}:")
    guess = int(input("> "))

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print(f"Good job, {name}! You got it in {attempt} guesses!")
        break

else:
    print(f"Nope! The number was {number}.")