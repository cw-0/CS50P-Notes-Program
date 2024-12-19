import csv

name = input("What's your name? ").title().strip()
game = input("What's your favorite game? ").title().strip()

with open("writecsv.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "game"])
    writer.writerow({"name": name, "game": game})

