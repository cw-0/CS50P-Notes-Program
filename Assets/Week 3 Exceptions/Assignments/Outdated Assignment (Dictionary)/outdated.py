import sys

month_text = {

"January": "01", 
"February": "02",
"March": "03",
"April": "04",
"May": "05",
"June": "06",
"July": "07",
"August": "08",
"September": "09",
"October": "10",
"November": "11",
"December": "12",

}


def main():
    while True:
        try:
            date_input = input("Date (MM/DD/YYYY): ".capitalize().strip())
        except EOFError:
            print("Closing")
            sys.exit()
        except Exception as e:
            print(f"Error: {e}")
            continue
        
        if "/" in date_input:
            try:
                month, day, year = date_input.split("/")
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                    break
                else:
                    print("error")
                    continue
            except ValueError:
                print("invalid format")
                continue
            except KeyError:
                print("invalid month name")

        elif "," in date_input:
            try:
                date_split, year = date_input.split(",")
                month, day = date_split.split(" ", 1)
                month = month.strip().capitalize()
                day = day.strip()
                year = year.strip()
                if 1 <= int(day) <= 31 and month in month_text:
                    print(f"{year}-{month_text[month]}-{int(day):02}")
                    break
                else:
                    print("error")
                    continue
            except ValueError:
                print("invalid format")
                continue
            except KeyError:
                print("invalid month name")
                continue

        else:
            print("invalid format")
            continue




main()