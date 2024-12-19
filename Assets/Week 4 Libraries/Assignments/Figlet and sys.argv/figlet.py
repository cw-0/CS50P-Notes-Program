from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        random_font()
    elif len(sys.argv) == 3 and(sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        select_font(sys.argv[2])
    else:
        sys.exit("Try figlet.py or figlet.py (-f or --font) font_name")

def random_font():
    font = random.choice(figlet.getFonts())
    prompt_print(font)


def select_font(font_name):
    if font_name in (figlet.getFonts()):
        prompt_print(font_name)
    else:
        sys.exit(f"Error: {font_name} is not a valid font")


def prompt_print(font):
    figlet.setFont(font=font)
    text = input("Input: ")
    print(f"Output: \n{figlet.renderText(text)}")

main()