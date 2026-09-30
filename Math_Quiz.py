import random

score = 0

print("Math Quiz")
print("Answer 5 questions!\n")

for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = a + b
    elif operation == "-":
        answer = a - b
    else:
        answer = a * b

    print(f"Question {i + 1}: {a} {operation} {b} = ")

    guess = int(input("> "))

    if guess == answer:
        print("Correct! 🎉")
        score += 1
    else:
        print(f"Nope! The answer was {answer}.")

    print()

print("Quiz finished!")
print(f"You got {score} out of 5 correct.")