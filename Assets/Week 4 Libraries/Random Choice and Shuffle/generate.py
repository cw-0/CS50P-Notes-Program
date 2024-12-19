import random

def main():
    pass



#Random Shuffle
def random_card():
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)


#Random Choice and Random Integer
def random_number():
    tag = random.choice([True, False])
    if tag == True:
        number = random.randint(1,10)
    else:
        number = random.randint(50, 60)
    print(number)


main()

