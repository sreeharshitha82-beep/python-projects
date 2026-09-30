import random

answers = [
    "Yes, definitely.",
    "It looks good.",
    "Probably.",
    "Ask me again later.",
    "I'm not sure.",
    "Don't count on it.",
    "Probably not.",
    "Nope.",
]

print("Magic 8 Ball")
print("Ask me anything!")

while True:
    question = input("\nYour question: ")

    if question == "":
        print("You need to ask a question.")
        continue

    print("Thinking...")
    print(random.choice(answers))

    again = input("\nAsk another question? (y/n): ").lower()

    if again != "y":
        print("See you!")
        break