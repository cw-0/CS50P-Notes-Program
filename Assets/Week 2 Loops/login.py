user = input("Whats is your username? ")

while True:
    print(f"User: {user}")
    password = input("Password: ")
    if password == "admin123":
        print(f"Hello, {user}")
        break
    else:
        print("invalid password")
        print("\n" * 2, end="")