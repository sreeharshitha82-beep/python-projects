import random

words = [
    "python",
    "airplane",
    "coffee",
    "guitar",
    "computer",
    "banana",
    "rocket",
    "student",
    "chocolate",
    "adventure"
]

word = random.choice(words)
scrambled = list(word)
random.shuffle(scrambled)
scrambled = "".join(scrambled)

print("Word Scramble")
print("Unscramble the letters to find the word!\n")

print("Scrambled word:", scrambled)

while True:
    guess = input("Your guess: ").lower()

    if guess == word:
        print("Correct! 🎉")
        break
    else:
        print("Nope! Try again.")

print("The word was:", word)