import re

name = input("Name: ").strip()
if validate := re.search(r"^(.+), ?(.+)$", name):
    last, first = validate.groups() # the groups being the (.+) in the re.search function
    name = f"{first} {last}"
print(f"Hello, {name}")

