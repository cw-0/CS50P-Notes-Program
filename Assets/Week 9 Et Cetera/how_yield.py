class Sheep:
    def __init__(self):
        pass


    def sheep(self, n):
        for i in range(n):
            yield"🐑" * i


def main():
    count_sheep = Sheep()
    n = int(input("What's n? "))
    for s in count_sheep.sheep(n):
        print(s)




if __name__ == "__main__":
    main()