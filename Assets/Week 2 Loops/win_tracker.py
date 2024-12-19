#Intro
print("Welcome to Win/Loss Tracker")
print("PLease select your game")

#Game Select
while True:
    game = input("Siege, UFC, Rocket League, Call Of Duty: ").strip().title()
    if game in ["Siege", "Ufc", "Rocket League", "Call Of Duty"]:
        break

#Spacing
print(".\n" * 3, end="")

#Main
print(f"{game} Tracker")

print("Please type W for game won and L for game lost. Type exit to quit")

W = 0

L = 0

while True:
    outcome = input("W/L: ").strip().capitalize()


    if outcome == "Exit":
        print("Exiting W/L Tracker")
        break

    if outcome == "W":
        W += 1

    elif outcome == "L":
        L += 1
    else:
        print("Please enter W, L, or Exit")
        continue

    print(f"Wins: {W}")
    print(f"Losses: {L}")