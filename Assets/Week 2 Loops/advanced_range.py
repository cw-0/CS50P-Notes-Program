import time

user = input("What would you like to say? ")
amount = int(input("How many times? "))

for _ in range(amount):
    print(user)
    time.sleep(.1)

new = input("Now try again with different coding method. What would you like to say? ")
i = int(input("How many times? "))

print(f"{new}\n" * i, end="")