
def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowel = ["a", "e", "i", "o", "u","A","E","I","O","U"]
    result = ""
    for letter in word:
        if letter not in vowel:
            result += letter
    return result


if __name__ == "__main__":
    main()