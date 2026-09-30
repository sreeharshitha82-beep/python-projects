import random

print("Coin Flip")

times = int(input("How many times do you want to flip? "))

heads = 0
tails = 0

for i in range(times):
    flip = random.choice(["Heads", "Tails"])

    print(flip)

    if flip == "Heads":
        heads += 1
    else:
        tails += 1

print()
print("Heads:", heads)
print("Tails:", tails)