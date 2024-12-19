def main():
    time = input("What time is it? ")
    clock = convert(time)
    if clock >= 7 and clock <= 8:
        print("Breakfast Time")
    elif clock >= 12 and clock <= 13:
        print("Lunch Time")
    elif clock >= 18 and clock <= 19:
        print("Dinner Time")
    else:
        exit()


def convert(time):
    hour, minute = map(float, time.split(":"))
    return hour + minute / 60

if __name__ == "__main__":
    main()