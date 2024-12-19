
students = [
    {"name": "Hermione", "house": "Griffindor"},
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Ron", "house": "Griffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]


houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)


homes = []
for house in houses:
    homes.append(house)

print(homes)
print(type(homes))