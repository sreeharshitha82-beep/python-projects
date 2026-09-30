import random
import time

print("Reaction Time Game")
print("Wait for GO, then press Enter as quickly as you can!")
input("\nPress Enter to start...")

wait = random.uniform(2, 5)

print("\nGet ready...")
time.sleep(wait)

print("GO!")

start = time.time()
input()
end = time.time()

reaction = end - start

print(f"\nYour reaction time was {reaction:.3f} seconds.")

if reaction < 0.2:
    print("WHAT. Are you a machine? 🤨")
elif reaction < 0.4:
    print("Pretty fast! ⚡")
elif reaction < 0.7:
    print("Not bad!")
else:
    print("Your reflexes need coffee. ☕")