import time

text = "Python is fun when you actually build things."

print("Typing Speed Test")
print("\nType this sentence:")
print(text)

input("\nPress Enter when you're ready...")

start = time.time()

answer = input("\nType it here:\n> ")

end = time.time()

time_taken = end - start

correct = 0

for i in range(min(len(text), len(answer))):
    if text[i] == answer[i]:
        correct += 1

accuracy = correct / len(text) * 100
words = len(answer.split())
speed = words / (time_taken / 60)

print()
print(f"Time: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Speed: {speed:.1f} words per minute")

if answer == text:
    print("Perfect! 🎉")
else:
    print("Not quite, but you'll get faster with practice.")