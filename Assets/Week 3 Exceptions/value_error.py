def main():
    x, sub, answer = get_int()
    print(f"{x} - {sub} = {answer}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("value is not an integer", end="\n\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            quit()
        else:
            print(f"x is {x}")
            try:
                sub = int(input("What would you like to subtract by? "))
            except ValueError:
                print("Value is not an integer\n\n")
            except KeyboardInterrupt:
                print("\nExiting...")
                quit()
            else:
                answer = x - sub
                return x, sub, answer


main()