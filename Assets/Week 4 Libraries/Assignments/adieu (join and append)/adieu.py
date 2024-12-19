import inflect
import sys

p = inflect.engine()

names = [

    
]

def main():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            format_names = p.join(names)
            sys.exit(f"Adieu, adieu, to {format_names}")

main()