import random


print('''Carrot in a Box

Two players. Two boxes. One carrot.

Player 1 gets to look inside their box and then
tries to convince Player 2 that they have the carrot.

Player 2 can then choose whether to swap boxes.
''')

input("Press Enter to start...")

p1 = input("Player 1, enter your name: ")
p2 = input("Player 2, enter your name: ")

names = p1[:11].center(11) + "    " + p2[:11].center(11)

print('''
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
''')

print(names)
print()

print(p1 + ", you have the RED box.")
print(p2 + ", you have the GOLD box.")
print()

print(p1 + ", you get to look inside your box.")
print(p2.upper() + ", close your eyes!")

input("Press Enter when Player 2 has closed their eyes...")

print()
print(p1 + ", here's what's inside your box:")

carrot = random.choice([True, False])

if carrot:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
   CARROT!
''')
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
  NO CARROT!
''')

print(names)

input("Press Enter to continue...")

print("\n" * 50)

print(p1 + ", tell " + p2 + " to open their eyes.")
input("Press Enter to continue...")

print()
print(p1 + ", choose what to tell " + p2 + ":")
print("1. There is a carrot in my box.")
print("2. There is no carrot in my box.")

input("Press Enter to continue...")

print()
print(p2 + ", do you want to swap boxes with " + p1 + "?")
print("Yes or No")

while True:
    answer = input("> ").lower()

    if answer.startswith("y") or answer.startswith("n"):
        break

    print("Please enter yes or no.")

first = "RED "
second = "GOLD"

if answer.startswith("y"):
    carrot = not carrot
    first, second = second, first

print('''
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
'''.format(first, second))

print(names)

input("Press Enter to reveal the winner...")

print()

if carrot:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
'''.format(first, second))

    print(p1 + " is the winner! 🥕")

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
'''.format(first, second))

    print(p2 + " is the winner! 🥕")

print("Thanks for playing!")