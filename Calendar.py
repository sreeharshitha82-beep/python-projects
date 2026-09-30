import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')


print('Calendar Maker')

while True:
    print('Enter the year:')
    answer = input('> ')

    if answer.isdecimal() and int(answer) > 0:
        year = int(answer)
        break

    print('Please enter a valid year.')


while True:
    print('Enter the month (1-12):')
    answer = input('> ')

    if answer.isdecimal() and 1 <= int(answer) <= 12:
        month = int(answer)
        break

    print('Please enter a number from 1 to 12.')


def make_calendar(year, month):
    text = ' ' * 34 + MONTHS[month - 1] + ' ' + str(year) + '\n'

    text += ('  Sunday     Monday    Tuesday   Wednesday   Thursday'
             '     Friday    Saturday\n')

    line = ('+----------' * 7) + '+\n'
    empty = ('|          ' * 7) + '|\n'

    date = datetime.date(year, month, 1)

    while date.weekday() != 6:
        date -= datetime.timedelta(days=1)

    while True:
        text += line

        row = ''

        for i in range(7):
            row += '|' + str(date.day).rjust(2) + ' ' * 8
            date += datetime.timedelta(days=1)

        text += row + '|\n'

        for i in range(3):
            text += empty

        if date.month != month:
            break

    text += line

    return text


calendar = make_calendar(year, month)

print(calendar)

filename = 'calendar_{}_{}.txt'.format(year, month)

with open(filename, 'w') as file:
    file.write(calendar)

print('Calendar saved as', filename)