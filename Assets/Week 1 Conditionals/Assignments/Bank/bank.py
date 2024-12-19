def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print("$", end="")
    print(result)



def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100






if __name__ == "__main__":
    main()
