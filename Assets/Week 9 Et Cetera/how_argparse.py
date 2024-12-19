import argparse

MEOWS = 3

parser = argparse.ArgumentParser(
    prog='how_argparse.py',
    description='Prints meow -n # times',
    epilog='For more info visit github.com/CodingCain',
)
parser.add_argument('-n', default=MEOWS, help="Number of times to meow", type=int)
args = parser.parse_args()


for i in range(int(args.n)):
    print("meow")


