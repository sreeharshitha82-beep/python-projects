# Tic-Tac-Toe

import random


def show(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def letter():
    l = ''

    while l != 'X' and l != 'O':
        print('Do you want to be X or O?')
        l = input().upper()

    if l == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def move(board, l, n):
    board[n] = l


def win(b, l):
    return (
        (b[7] == l and b[8] == l and b[9] == l) or
        (b[4] == l and b[5] == l and b[6] == l) or
        (b[1] == l and b[2] == l and b[3] == l) or
        (b[7] == l and b[4] == l and b[1] == l) or
        (b[8] == l and b[5] == l and b[2] == l) or
        (b[9] == l and b[6] == l and b[3] == l) or
        (b[7] == l and b[5] == l and b[3] == l) or
        (b[9] == l and b[5] == l and b[1] == l)
    )


def copy(board):
    new = []

    for x in board:
        new.append(x)

    return new


def free(board, n):
    return board[n] == ' '


def playerMove(board):
    n = ' '

    while n not in '1 2 3 4 5 6 7 8 9'.split() or not free(board, int(n)):
        print('What is your next move? (1-9)')
        n = input()

    return int(n)


def randomMove(board, moves):
    possible = []

    for n in moves:
        if free(board, n):
            possible.append(n)

    if len(possible) > 0:
        return random.choice(possible)

    return None


def computerMove(board, c):
    if c == 'X':
        p = 'O'
    else:
        p = 'X'

    # Can the computer win?
    for n in range(1, 10):
        test = copy(board)

        if free(test, n):
            move(test, c, n)

            if win(test, c):
                return n

    # Can the player win? Block them.
    for n in range(1, 10):
        test = copy(board)

        if free(test, n):
            move(test, p, n)

            if win(test, p):
                return n

    # Take a corner.
    n = randomMove(board, [1, 3, 7, 9])

    if n != None:
        return n

    # Take the center.
    if free(board, 5):
        return 5

    # Take a side.
    return randomMove(board, [2, 4, 6, 8])


def full(board):
    for n in range(1, 10):
        if free(board, n):
            return False

    return True


print('Welcome to Tic-Tac-Toe!')


while True:

    board = [' '] * 10

    p, c = letter()

    turn = first()

    print('The ' + turn + ' will go first.')

    playing = True

    while playing:

        if turn == 'player':

            show(board)

            n = playerMove(board)

            move(board, p, n)

            if win(board, p):
                show(board)
                print('Hooray! You won!')
                playing = False

            elif full(board):
                show(board)
                print('The game is a tie!')
                break

            else:
                turn = 'computer'

        else:

            n = computerMove(board, c)

            move(board, c, n)

            if win(board, c):
                show(board)
                print('The computer won! You lose.')
                playing = False

            elif full(board):
                show(board)
                print('The game is a tie!')
                break

            else:
                turn = 'player'

    print('Do you want to play again? (yes or no)')

    if not input().lower().startswith('y'):
        break