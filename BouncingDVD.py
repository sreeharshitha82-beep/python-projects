import sys
import random
import time

try:
    import bext
except ImportError:
    print('This program needs the "bext" module.')
    print('Install it with: pip install bext')
    sys.exit()


WIDTH, HEIGHT = bext.size() 
WIDTH -= 1

LOGOS = 5
PAUSE = 0.2

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'

DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


def main():
    bext.clear()

    logos = []

    for i in range(LOGOS):
        x = random.randint(1, WIDTH - 4)
        y = random.randint(1, HEIGHT - 4)

        if x % 2 == 1:
            x -= 1

        logo = {
            'color': random.choice(COLORS),
            'x': x,
            'y': y,
            'direction': random.choice(DIRECTIONS)
        }

        logos.append(logo)

    corners = 0

    while True:
        for logo in logos:
            bext.goto(logo['x'], logo['y'])
            print('   ', end='')

            old_direction = logo['direction']

            x = logo['x']
            y = logo['y']
            direction = logo['direction']

            if x == 0 and y == 0:
                direction = DOWN_RIGHT
                corners += 1

            elif x == 0 and y == HEIGHT - 1:
                direction = UP_RIGHT
                corners += 1

            elif x == WIDTH - 3 and y == 0:
                direction = DOWN_LEFT
                corners += 1

            elif x == WIDTH - 3 and y == HEIGHT - 1:
                direction = UP_LEFT
                corners += 1

            elif x == 0 and direction == UP_LEFT:
                direction = UP_RIGHT

            elif x == 0 and direction == DOWN_LEFT:
                direction = DOWN_RIGHT

            elif x == WIDTH - 3 and direction == UP_RIGHT:
                direction = UP_LEFT

            elif x == WIDTH - 3 and direction == DOWN_RIGHT:
                direction = DOWN_LEFT

            elif y == 0 and direction == UP_LEFT:
                direction = DOWN_LEFT

            elif y == 0 and direction == UP_RIGHT:
                direction = DOWN_RIGHT

            elif y == HEIGHT - 1 and direction == DOWN_LEFT:
                direction = UP_LEFT

            elif y == HEIGHT - 1 and direction == DOWN_RIGHT:
                direction = UP_RIGHT

            logo['direction'] = direction

            if direction != old_direction:
                logo['color'] = random.choice(COLORS)

            if direction == UP_RIGHT:
                logo['x'] += 2
                logo['y'] -= 1

            elif direction == UP_LEFT:
                logo['x'] -= 2
                logo['y'] -= 1

            elif direction == DOWN_RIGHT:
                logo['x'] += 2
                logo['y'] += 1

            elif direction == DOWN_LEFT:
                logo['x'] -= 2
                logo['y'] += 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corners, end='')

        for logo in logos:
            bext.goto(logo['x'], logo['y'])
            bext.fg(logo['color'])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo')
        sys.exit()