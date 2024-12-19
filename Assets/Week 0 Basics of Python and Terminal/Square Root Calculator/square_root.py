import sys


def main():
    print("Welcome to square_root.py!")
    x = int(input("What's x? "))
    print(f"x squared is: {square_root(x)}")


def square_root(n):
    if n <= 0:
        print("Negative numbers not allowed")
        sys.exit()
    else:
        n = n**0.5
        if n.is_integer():
            return str(int((n)))
        else:
            return f"{n:.2f}"


main()
