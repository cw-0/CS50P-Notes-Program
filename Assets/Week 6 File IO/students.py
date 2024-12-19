import csv

peoples = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        peoples.append({"name": row["name"], "age": row["age"], "job": row["job"]})

for people in sorted(peoples, key=lambda student: student["name"]):
    if people["job"] != "none":
        print(f"{people['name']} is {people['age']} and works at {people['job']}")
    else:
        print(f"{people['name']} is {people['age']} and is Unemployed")

