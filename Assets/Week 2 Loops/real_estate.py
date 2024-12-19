import getpass
import webbrowser
import time

def login():
    while True:
        user = input("Username: ").strip().lower()

        password = getpass.getpass("Password: ")

        if user == "macy" and password == "md240199":
            break
        else:
            print("invalid login")

login()

while True:
    print("               ___________________________")
    print("              | Welcome to Macs Enterprise|")
    print("              |                           |")
    print("              | What would you like to do?|")
    print("               ...........................")
    choices = print("       My Properties   Banking   Tenants   Email")
    print()
    print("                   or type exit to quit")
    print("\n" * 3 )
    select = input("Select: ").strip().lower()
    if "my properties" in select:
        webbrowser.open('https://www.kw.com/')
    elif "banking" in select:
        webbrowser.open('https://Arvest.com/')
    elif "tenants" in select:
        webbrowser.open('https://docs.google.com/document/u/0/?pli=1')
    elif "Email" in select:
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    elif "exit" in select:
        print("Closing application...")
        break
    else:
        print("Unknown selection. Please check spelling and try again.")
        time.sleep(3)
        print()

