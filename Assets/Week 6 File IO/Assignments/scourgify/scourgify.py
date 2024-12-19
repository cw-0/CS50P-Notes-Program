import csv
import sys


characters = []


def main():
    old_file, new_file = get_file()
    open_file(old_file)
    make_new(new_file)
    print("\033[92mDone\033[0m!")



def get_file():
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    return sys.argv[1], sys.argv[2]

def open_file(old_file): # reads old file (name and house)
    try:
        with open(old_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row['name'].split(", ")
                characters.append({"first": first, "last": last, "house": row['house']})
    except FileNotFoundError:
        sys.exit("File not found")



def make_new(new_file): # writes new file (first, last, house)
    with open(new_file, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for character in characters:
            writer.writerow(character)

if __name__ == "__main__":
    main()