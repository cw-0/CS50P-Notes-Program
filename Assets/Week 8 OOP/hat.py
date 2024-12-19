import random
import os
import sys


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        if not name.strip():
            raise ValueError("Insert Name")
        house = random.choice(cls.houses)
        print(name, "is in", house)

def main():      
    while True:
        try:
            name = input("Name: ").strip()
            Hat.sort(name)
            break
        except ValueError as e:
            print(f"Error: {e}")
            input("Press  Enter to try again...")
            clear_console()
            continue


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()