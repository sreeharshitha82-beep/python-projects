import random
import string

print("Random Password Generator")

length = int(input("How long should the password be? "))

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*"

chars = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(chars)

print("\nYour password is:")
print(password)

