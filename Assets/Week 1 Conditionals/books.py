import time

select = input("What would you like to track? Books/Game: ").lower()

if "books" in select:
    name = input("Name of book: ").strip().title()

    pages = float(input("Number of pages: "))

    days = float(input(f"How many days do you want it to take you to read {name}? "))

    total = pages / days

    print(f"It will take you {total:.0f} pages a day to read {name} in {days:.0f} days")
    print("...")
    time.sleep(2)

    read = input("Would you like to start reading today? (y/n): ").strip().lower()
    if read in ["y", "yes"]:
        print("Starting Read Log")
        log = open(f"{name}.txt", "w")
        log.write(f"{name}\n{total}")

    elif read in ["n", "no"]:
        print("Thank you for using Cains Tracker! Now Closing...")
        exit()
    else:
        print("Error coming soon")



 #implement a way to mark off reading for that day and at the top ask if already started reading and what page they're on

