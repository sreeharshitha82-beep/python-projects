import datetime
import random


def get_birthdays(num):
    birthdays = []
    start = datetime.date(2001, 1, 1)

    for i in range(num):
        days = datetime.timedelta(random.randint(0, 364))
        birthday = start + days
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, birthday in enumerate(birthdays):
        for other in birthdays[i + 1:]:
            if birthday == other:
                return birthday


months = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
)


print('''Birthday Paradox

Let's see how likely it is for two people to
have the same birthday.

We will generate random birthdays and run
the experiment many times.
''')


while True:
    print('How many people should we generate? (1-100)')
    answer = input('> ')

    if answer.isdecimal() and 0 < int(answer) <= 100:
        num = int(answer)
        break


print()
print('Here are the birthdays:')

birthdays = get_birthdays(num)

for i, birthday in enumerate(birthdays):
    if i > 0:
        print(', ', end='')

    month = months[birthday.month - 1]
    print('{} {}'.format(month, birthday.day), end='')

print('\n')


match = get_match(birthdays)

if match:
    month = months[match.month - 1]
    print('We have a matching birthday: {} {}'.format(month, match.day))
else:
    print('No matching birthdays this time.')

print()
print('Now let\'s run the experiment 100,000 times.')
input('Press Enter to start...')

matches = 0

for i in range(100_000):
    birthdays = get_birthdays(num)

    if get_match(birthdays):
        matches += 1

print('Done!')

chance = round(matches / 100_000 * 100, 2)

print()
print('Out of 100,000 groups of {} people:'.format(num))
print('{} groups had at least one matching birthday.'.format(matches))
print('That means the chance is about {}%.'.format(chance))