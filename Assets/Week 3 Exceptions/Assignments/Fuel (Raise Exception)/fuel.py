# test

def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x, y = convert(fraction)
            percentage = float(x / y) * 100
            percentage = int(round(percentage))
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError, TooBigError) as e:
            print(e)





def convert(fraction):
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y and y != 0:
                raise TooBigError("x cannot be greater than y")
            if y == 0:
                raise ZeroDivisionError("y cannot be 0")
        except ValueError:
            raise ValueError("Error. Try using an integer")
        return x, y
            





def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(f"{percentage}%")

    


class TooBigError(Exception):
    pass




if __name__ == "__main__":
    main()
