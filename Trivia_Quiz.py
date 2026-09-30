questions = [
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "How many planets are in our solar system?",
        "answer": "8"
    },
    {
        "question": "What is 12 × 12?",
        "answer": "144"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars"
    },
    {
        "question": "What language are you currently learning?",
        "answer": "python"
    }
]

score = 0

print("Trivia Quiz")
print("Let's see how much you know!\n")

for question in questions:
    answer = input(question["question"] + " ").lower().strip()

    if answer == question["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Nope!")
        print("The answer was:", question["answer"])

    print()

print("Quiz finished!")
print(f"You got {score} out of {len(questions)} correct.")

percentage = score / len(questions) * 100
print(f"Your score: {percentage:.0f}%")