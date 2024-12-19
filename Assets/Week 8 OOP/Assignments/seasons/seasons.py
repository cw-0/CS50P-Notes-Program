import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    birth_date = input("Birthdate 'YYYY-MM-DD': ").strip()
    time_elapsed = get_time(birth_date)
    result = convert_number(time_elapsed)
    print(f"{result} minutes have passed")


def validate_user_date(birth_date):
    try:
        date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid Format. Please use 'YYYY-MM-DD'.")


def get_time(birth_date):
    if birth_date.count("-") == 2:
        birth_year, birth_month, birth_day = birth_date.split("-")
        formatted_birthdate = date(int(birth_year), int(birth_month), int(birth_day))

        today = date.today()
        birth = (today - formatted_birthdate).total_seconds() / 60
        return int(birth)
    else:
        sys.exit("Invalid Format. Please use 'YYYY-MM-DD'.")


def convert_number(time_elapsed):
    word_form = f"{p.number_to_words(time_elapsed, andword='')} minutes have passed"
    return word_form


if __name__ == "__main__":
    main()