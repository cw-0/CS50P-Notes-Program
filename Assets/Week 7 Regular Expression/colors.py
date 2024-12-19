import re

# regex

def main():
    code = input("Hexadecimal color code: ").strip()

    match = re.search(r"^#{1}([0-9]|f){6}$", code, flags=re.I)
    if match:
        print(code.upper())
    else:
        print("Invalid")



if __name__== "__main__":
    main()
