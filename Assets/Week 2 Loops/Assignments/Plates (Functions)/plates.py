def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) < 7:
        if s[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and s[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if " " not in s:
                if not any(char in "./?@[]!$#&" for char in s):
                    if found_number(s):
                        return True
                    elif not any(char.isdigit() for char in s):
                        return True
    return False


def found_number(s):
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and not found_number:
                return False
            found_number = True
        elif char.isalpha() and found_number:
            return False
    return found_number



if __name__ == "__main__":
    main()
