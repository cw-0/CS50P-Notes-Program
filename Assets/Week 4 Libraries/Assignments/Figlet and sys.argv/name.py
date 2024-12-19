import sys



def main():
    names = sys.argv[1:]
    for name in names:
        print(f"welcome, {name}")


if __name__ == "__main__":
    main()

    