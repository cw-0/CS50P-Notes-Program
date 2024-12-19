
# Squaring Calculator

def main():
    x = int(input("Whats x? "))
    print(f"{x} squared is {square(x)}")
    input("Press Enter to close")

def square(n):
    return n * n

if __name__ == "__main__":
    main()
