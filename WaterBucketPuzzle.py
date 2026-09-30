import sys


GOAL = 4
steps = 0

water = {
    '8': 0,
    '5': 0,
    '3': 0
}


while True:
    print()
    print('Try to get {}L of water into one of the buckets.'.format(GOAL))

    display = []

    for size in ('8', '5', '3'):
        for level in range(1, int(size) + 1):
            if water[size] >= level:
                display.append('WWWWWW')
            else:
                display.append('      ')

    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*display))

    if GOAL in water.values():
        print('You solved it in {} steps!'.format(steps))
        sys.exit()

    print('What do you want to do?')
    print('(F)ill')
    print('(E)mpty')
    print('(P)our')
    print('(Q)uit')

    while True:
        move = input('> ').upper()

        if move in ('F', 'E', 'P'):
            break

        if move in ('Q', 'QUIT'):
            print('Thanks for playing!')
            sys.exit()

        print('Please enter F, E, P, or Q.')

    while True:
        print('Choose a bucket: 8, 5, or 3')
        source = input('> ')

        if source in water:
            break

        if source.upper() in ('Q', 'QUIT'):
            print('Thanks for playing!')
            sys.exit()

        print('Please choose 8, 5, or 3.')

    if move == 'F':
        water[source] = int(source)
        steps += 1

    elif move == 'E':
        water[source] = 0
        steps += 1

    elif move == 'P':
        while True:
            print('Pour into which bucket? 8, 5, or 3')
            target = input('> ')

            if target in water:
                break

            print('Please choose 8, 5, or 3.')

        target_size = int(target)
        space = target_size - water[target]
        amount = min(space, water[source])

        water[source] -= amount
        water[target] += amount

        steps += 1

