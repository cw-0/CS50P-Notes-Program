import re
import sys



def main():
    print(count(input("Text: ")))


def count(s):
    um_count = 0
    match = re.findall(r"\bum\b", s, flags=re.I)
    return len(match)


if __name__ == "__main__":
    main()