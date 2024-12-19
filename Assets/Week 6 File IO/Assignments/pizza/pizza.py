import sys
import csv
from tabulate import tabulate


table = []



def main():
    location = get_file()
    open_file(location)



def get_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    return sys.argv[1]


def open_file(location):
    check1, check2 = location.split(".")
    if check2 == "csv":
        try:
            with open(location, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                rows = [row for row in reader]
                print(tabulate(rows, headers=header, tablefmt='grid'))
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Not a csv file")












if __name__ == "__main__":
    main()
