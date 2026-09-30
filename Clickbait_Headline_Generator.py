import random

pronouns = ["Her", "Him", "Them"]
possessive = ["Her", "His", "Their"]
personal = ["She", "He", "They"]

states = [
    "California", "Texas", "Florida", "New York", "Pennsylvania",
    "Illinois", "Ohio", "Georgia", "North Carolina", "Michigan"
]

nouns = [
    "Athlete", "Clown", "Shovel", "Paleo Diet", "Doctor", "Parent",
    "Cat", "Dog", "Chicken", "Robot", "Video Game", "Avocado",
    "Plastic Straw", "Serial Killer", "Telephone Psychic"
]

places = [
    "House", "Attic", "Bank Deposit Box", "School",
    "Basement", "Workplace", "Donut Shop", "Apocalypse Bunker"
]

when = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]

print("Clickbait Headline Generator")
print("Let's make some terrible headlines. 📰\n")

while True:
    amount = input("How many headlines do you want? ")

    if amount.isdecimal():
        amount = int(amount)
        break

    print("Please enter a number.")

print()

for i in range(amount):
    choice = random.randint(1, 8)

    if choice == 1:
        noun = random.choice(nouns)
        headline = f"Are Millennials Killing the {noun} Industry?"

    elif choice == 2:
        noun = random.choice(nouns)
        plural = random.choice(nouns) + "s"
        time = random.choice(when)
        headline = f"Without This {noun}, {plural} Could Kill You {time}"

    elif choice == 3:
        pronoun = random.choice(pronouns)
        state = random.choice(states)
        noun1 = random.choice(nouns)
        noun2 = random.choice(nouns)
        headline = f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}"

    elif choice == 4:
        state = random.choice(states)
        noun = random.choice(nouns)
        pronoun = random.choice(possessive)
        place = random.choice(places)
        headline = f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"

    elif choice == 5:
        noun1 = random.choice(nouns) + "s"
        noun2 = random.choice(nouns) + "s"
        headline = f"What {noun1} Don't Want You To Know About {noun2}"

    elif choice == 6:
        number = random.randint(7, 15)
        noun = random.choice(nouns)
        state = random.choice(states)
        headline = f"{number} Gift Ideas to Give Your {noun} From {state}"

    elif choice == 7:
        number1 = random.randint(3, 19)
        noun = random.choice(nouns) + "s"
        number2 = random.randint(1, number1)
        headline = f"{number1} Reasons Why {noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"

    else:
        state = random.choice(states)
        noun = random.choice(nouns)
        i = random.randint(0, 2)

        pronoun1 = possessive[i]
        pronoun2 = personal[i]

        if pronoun1 == "Their":
            headline = f"This {state} {noun} Didn't Think Robots Would Take Their Job. They Were Wrong."
        else:
            headline = f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong."

    print(headline)

print()

website = random.choice([
    "Wobsite",
    "Blag",
    "Facebuuk",
    "Googles",
    "Facesbook",
    "Tweedie",
    "Pastagram"
])

time = random.choice(when).lower()

print(f"Post these to our {website} {time} or you're fired! 💀")
