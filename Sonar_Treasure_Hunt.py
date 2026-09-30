# Sonar Treasure Hunt

import random
import sys
import math


WIDTH = 60
HEIGHT = 15
CHESTS = 3
SONAR = 20


def newBoard():
    board = []

    for x in range(WIDTH):
        board.append([])

        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def show(board):
    # Print the numbers at the top.

    top = '    '

    for i in range(1, 6):
        top += (' ' * 9) + str(i)

    print(top)
    print('   ' + ('0123456789' * 6))
    print()

    # Print the board.

    for y in range(HEIGHT):

        if y < 10:
            space = ' '
        else:
            space = ''

        row = ''

        for x in range(WIDTH):
            row += board[x][y]

        print('%s%s %s %s' % (space, y, row, y))

    # Print the numbers at the bottom.

    print()
    print('   ' + ('0123456789' * 6))
    print(top)


def getChests(num):
    chests = []

    while len(chests) < num:

        chest = [
            random.randint(0, WIDTH - 1),
            random.randint(0, HEIGHT - 1)
        ]

        if chest not in chests:
            chests.append(chest)

    return chests


def onBoard(x, y):
    return (
        x >= 0 and
        x < WIDTH and
        y >= 0 and
        y < HEIGHT
    )


def move(board, chests, x, y):
    # Find the distance to the closest chest.

    closest = 100

    for cx, cy in chests:

        distance = math.sqrt(
            (cx - x) * (cx - x) +
            (cy - y) * (cy - y)
        )

        if distance < closest:
            closest = distance

    closest = round(closest)

    # If we are directly on a chest.

    if closest == 0:
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'

    # If the chest is within sonar range.

    if closest < 10:
        board[x][y] = str(closest)

        return (
            'Treasure detected at a distance of %s '
            'from the sonar device.'
            % closest
        )

    # If the chest is too far away.

    board[x][y] = 'X'

    return (
        'Sonar did not detect anything. '
        'All treasure chests out of range.'
    )


def playerMove(old):
    print(
        'Where do you want to drop the next sonar device? '
        '(0-59 0-14) (or type quit)'
    )

    while True:

        text = input()

        if text.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        text = text.split()

        if (
            len(text) == 2
            and text[0].isdigit()
            and text[1].isdigit()
            and onBoard(int(text[0]), int(text[1]))
        ):

            x = int(text[0])
            y = int(text[1])

            if [x, y] in old:
                print('You already moved there.')
                continue

            return [x, y]

        print(
            'Enter a number from 0 to 59, a space, '
            'then a number from 0 to 14.'
        )


def instructions():

    print('''Instructions:

You are the captain of the Simon, a treasure-hunting ship.
Your mission is to use sonar devices to find three sunken
treasure chests at the bottom of the ocean.

But you only have cheap sonar that finds distance,
not direction.

Enter the coordinates to drop a sonar device.
The ocean map will show how far away the nearest chest is.

For example:

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

          012345678901234567890123456789012
                    1         2         3

(In the real game, the chests are not visible.)

Press enter to continue...''')

    input()

    print('''

When you drop a sonar device directly on a chest,
you retrieve it.

The other sonar devices will update to show how far
away the next nearest chest is.

Sonar can detect treasure up to a distance of 9 spaces.

Try to collect all 3 chests before running out
of sonar devices.

Good luck!

Press enter to continue...''')

    input()


print('S O N A R!')
print()

print('Would you like to view the instructions? (yes/no)')

if input().lower().startswith('y'):
    instructions()


while True:

    # Set up the game.

    sonar = SONAR
    board = newBoard()
    chests = getChests(CHESTS)

    show(board)

    old = []

    # Main game loop.

    while sonar > 0:

        print(
            'You have %s sonar device(s) left. '
            '%s treasure chest(s) remaining.'
            % (sonar, len(chests))
        )

        # Get player's coordinates.

        x, y = playerMove(old)

        old.append([x, y])

        # Use sonar.

        result = move(board, chests, x, y)

        # If a chest was found, update all old sonar positions.

        if result == 'You have found a sunken treasure chest!':

            for x, y in old:
                move(board, chests, x, y)

        show(board)

        print(result)

        # Did we find all the chests?

        if len(chests) == 0:

            print(
                'You have found all the sunken treasure chests! '
                'Congratulations and good game!'
            )

            break

        sonar -= 1

    # If we ran out of sonar.

    if sonar == 0:

        print(
            "We've run out of sonar devices! "
            "Now we have to turn the ship around and head"
        )

        print(
            'for home with treasure chests still out there! '
            'Game over.'
        )

        print('    The remaining chests were here:')

        for x, y in chests:
            print('    %s, %s' % (x, y))

    # Play again?

    print('Do you want to play again? (yes or no)')

    if not input().lower().startswith('y'):
        sys.exit()