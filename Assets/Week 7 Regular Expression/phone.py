import re
locations = {"+1": "United States and Canada", "+62": "Indoneasia", "+505": "Nicaragua"}

def main():
    pattern = r"^(?P<area>\+\d{1,3}) \d{3}-\d{3}-\d{4}$"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        try:
            country = (locations[match.group("area")])
            print(f"Phone registered in {country}")
        except KeyError:
            print("Invalid area code.")
    else:
        print("Invalid\nUse +\"area code\" ###-###-####")


if __name__ == "__main__":
    main()