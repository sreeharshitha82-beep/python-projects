import random

DIGITS = 3
GUESSES = 10


def main():
    print('''Welcome to Bagels!

I'm thinking of a {}-digit number with no repeated digits.
Try to guess it!

Pico  = right digit, wrong position
Fermi = right digit, right position
Bagels = no correct digits

You have {} guesses. Good luck!
'''.format(DIGITS, GUESSES))

    while True:
        secret = get_secret()

        count = 1

        while count <= GUESSES:
            print('Guess #{}:'.format(count))
            guess = input('> ')

            while len(guess) != DIGITS or not guess.isdecimal():
                print('Please enter a {}-digit number.'.format(DIGITS))
                guess = input('> ')

            clues = get_clues(guess, secret)
            print(clues)

            if guess == secret:
                break

            count += 1

        if guess != secret:
            print("Out of guesses! The number was {}.".format(secret))

        print('\nWant to play again? (yes/no)')
        answer = input('> ')

        if not answer.lower().startswith('y'):
            break

        print()

    print('Thanks for playing!')


def get_secret():
    nums = list('0123456789')
    random.shuffle(nums)

    secret = ''

    for i in range(DIGITS):
        secret += nums[i]

    return secret


def get_clues(guess, secret):
    if guess == secret:
        return 'You got it! 🎉'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append('Fermi')
        elif guess[i] in secret:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main()