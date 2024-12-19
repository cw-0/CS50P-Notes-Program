import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except Exception as e:
            continue
    game(level)

def game(level):
    answer = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
        except Exception as e:
            continue
        except EOFError:
            sys.exit("Exiting)")
        if guess < 0:
            continue
        elif guess < answer:
            print("Too small!")
            continue
        elif guess > answer:
            print("Too large!")
            continue
        elif guess == answer:
            print("Just right!")
            break
        else:
            print("Error with your answer")
    sys.exit()



main()