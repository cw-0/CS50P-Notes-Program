cars = [
    {"Car": "Octane", "Tier": "S Tier", "Used By": "Pro 1"},
    {"Car": "Dominus", "Tier": "S Tier", "Used By": "Cain"},
    {"Car": "Batmobile", "Tier": "A Tier", "Used By": None},
    {"Car": "Takuma", "Tier": "D Tier", "Used By": "Pro 2"},
    {"Car": "Scarab", "Tier": "Meme Tier", "Used By": None},
]

print()

for car in cars:
    print(car["Car"], car["Tier"], car["Used By"], sep=", ", end="\n \n")