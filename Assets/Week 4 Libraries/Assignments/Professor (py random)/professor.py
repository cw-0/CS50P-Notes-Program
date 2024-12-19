import random
import sys

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except Exception as e:
            continue
        if level in range(1, 4):
            return level
        else:
            continue


def generate_integer(level):

    question = 0
    score = 0

    while question < 10:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            answer = x + y
            attempt = 1
            while attempt < 4:
                try:
                    problem = int(input(f"{x} + {y} = "))
                    if problem == answer:
                        score += 1
                        break
                    else:
                        print("EEE")
                        attempt += 1
                except ValueError:
                            print("Invalid input. Please enter a number")

            if attempt > 3:
                print(f"{x} + {y} = {answer}")

        elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
                answer = x + y
                attempt = 1
                while attempt < 4:
                    try:
                        problem = int(input(f"{x} + {y} = "))
                        if problem == answer:
                            score += 1
                            break
                        else:
                            print("EEE")
                            attempt += 1
                    except ValueError:
                                print("Invalid input. Please enter a number")

                if attempt > 3:
                    print(f"{x} + {y} = {answer}")
        elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
                answer = x + y
                attempt = 1
                while attempt < 4:
                    try:
                        problem = int(input(f"{x} + {y} = "))
                        if problem == answer:
                            score += 1
                            break
                        else:
                            print("EEE")
                            attempt += 1
                    except ValueError:
                                print("Invalid input. Please enter a number")

                if attempt > 3:
                    print(f"{x} + {y} = {answer}")

        question += 1
    return score



if __name__ == "__main__":
    main()
