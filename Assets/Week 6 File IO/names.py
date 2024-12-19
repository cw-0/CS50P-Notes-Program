with open("names.txt", "r") as file:
    for name in sorted(file, reverse = True):
        print(f"Hello, {name.rstrip()}")
