import time

text = input("What would you like to say? ")
amount = int(input("How many times? "))
speed = float(input("How fast (seconds in between): "))

while amount != 0 and amount >= 0:
    print(text)
    time.sleep(speed)
    amount -= 1
if amount < 0:
    print("Be for real...")