print("Reverse Number Guessing")
print("Think of a number between 1 and 100.")
print("I'll try to guess it.")

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1

    print(f"\nIs your number {guess}?")
    answer = input("Enter h for higher, l for lower, or c for correct: ").lower()

    if answer == "c":
        print(f"I got it! Your number was {guess}.")
        print(f"It took me {attempts} guesses.")
        break

    elif answer == "h":
        low = guess + 1

    elif answer == "l":
        high = guess - 1

    else:
        print("Please enter h, l, or c.")
        attempts -= 1

    if low > high:
        print("Something went wrong. You changed your answer.")
        break