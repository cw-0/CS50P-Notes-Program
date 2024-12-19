from validator_collection import validators, checkers, errors


def main():
    try:
        print(email_checker(input("Email: ").strip().lower()))
    except ValueError as e:
        print(e)


def email_checker(s):
    try:
        validators.email(s)
        return  "Valid"
    except errors.InvalidEmailError:
        raise ValueError("Invalid Email")
    

if __name__ == "__main__":
    main()