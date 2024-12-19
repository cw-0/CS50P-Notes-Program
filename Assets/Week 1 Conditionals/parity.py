def main():
    age = int(input("How old are you? "))
    if is_even(age):
        print("Your age is even")
    else:
        print("Your age is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:                  ## only in python can you instead make this
        return False       ## return True if n % 2 == 0 else False

#condensed return n % 2 == 0



main()