import emoji


def main():
    raw = input("Input: ")
    out = emoji.emojize(raw, language="alias")
    print(out)



if __name__ == "__main__":
    main()