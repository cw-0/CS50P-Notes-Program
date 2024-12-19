print("Fruit Calories Information")
print('for list of available items please type "help"')
item = input("Item: ").lower().strip()

if "apple" in item:
    print("130 calories")
elif item in ["avocado", "cantaloupe", "honeydew melon", "pineapple", "strawberries", "tangerine"]:
    print("50 calories")
elif "banana" in item:
    print("110 calories")
elif item in ["grapefuit", "nectarine", "peach"]:
    print("60 calories")
elif item in ["grapes", "kiwifruit"]:
    print("90 calories")
elif "lemon" in item:
    print("15 calories")
elif "lime" in item:
    print("20 calories")
elif item in ["orange", "watermelon"]:
    print("80 calories")
elif item in ["pear", "sweet cherries"]:
    print("100 calories")
elif "plums" in item:
    print("70 calories")
else:
    quit()