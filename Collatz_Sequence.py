print("Collatz Sequence")
print("Start with a number and watch what happens!\n")

while True:
    number = input("Enter a number greater than 0: ")

    if number.isdecimal() and int(number) > 0:
        number = int(number)
        break

    print("Please enter a valid positive number.")

print("\nSequence:")

while number != 1:
    print(number, end=" → ")

    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

print(1)
print("\nDone! 🎉")