import sys



def main():
    location = get_file()
    lines = open_file(location)
    n = count_lines(lines)
    print(f"{location} has {n} lines of code")



def get_file():
    if len(sys.argv)> 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    return sys.argv[1]


def open_file(location):
    lines = []
    check1, check2 = location.split(".")
    if check2 == "py":
        try:
            with open(f"{location}", "r") as file:
                for line in file:
                    lines.append(line)
            return lines
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("invalid file format")

def count_lines(lines):
    n = 0
    for line in lines:
        if line.strip() and line.lstrip().startswith("#") == False:
            n += 1
    return n


if __name__ == "__main__":
    main()
