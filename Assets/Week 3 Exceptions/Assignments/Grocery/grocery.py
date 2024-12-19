import sys



def main():

    grocery_list = {


    }
    while True:
        try:
            item = input().strip().lower()
        except EOFError:
            for item in sorted(grocery_list):
                print(f"{grocery_list[item]} {item.upper()}")
            sys.exit()
        except KeyError:
            pass
        else:
            grocery_list[item] = grocery_list.get(item, 0) + 1



main()