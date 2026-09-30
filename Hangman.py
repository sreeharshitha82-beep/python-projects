import random

words = ['python', 'computer', 'programming', 'hangman', 'dragon']

word = random.choice(words)
guessed = []
wrong = 0

hangman = [
r"""
  +---+
      |
      |
      |
     ===
""",
r"""
  +---+
  O   |
      |
      |
     ===
""",
r"""
  +---+
  O   |
  |   |
      |
     ===
""",
r"""
  +---+
  O   |
 /|   |
      |
     ===
""",
r"""
  +---+
  O   |
 /|\  |
      |
     ===
""",
r"""
  +---+
  O   |
 /|\  |
 /    |
     ===
""",
r"""
  +---+
  O   |
 /|\  |
 / \  |
     ===
"""
]

print("HANGMAN")
print("Try to guess the word!")

while wrong < 6:
    print(hangman[wrong])

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if all(letter in guessed for letter in word):
        print("You won! 🎉")
        print("The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice! That's in the word.")
    else:
        wrong += 1
        print("Nope! That's not in the word.")

else:
    print(hangman[6])
    print("You lost! 💀")
    print("The word was:", word)