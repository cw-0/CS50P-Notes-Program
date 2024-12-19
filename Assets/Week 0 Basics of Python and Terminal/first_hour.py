import time

#Greeting
print("Thank you for visiting My Website on Desktop")
time.sleep(1.2)
print("Please answer the following questions with either Yes or No")
time.sleep(1.2)

#Existing User

while True:
    Customer = input("Are you a returning customer? ").lower().strip()
    if Customer in ["yes", "no"]:
        break
    else:
        time.sleep(1)
        print("Please answer this with Yes or No.")
        time.sleep(1)

if Customer == "yes":
    Name = input("What is your full name? ").strip().title()
    print(f"Welcome back, {Name}") ##Special Formating

    first, last = Name.split(" ")

    print(first + " these are our newest products.") ## or print(f"{first} these are our newest products.")


#New User

elif Customer == "no":
    New_User = input("Would you like to sign up? ").lower().strip()
    if New_User == "yes":
        Name = input("What is your full name? ").strip().title()
        print("Thank You for signing up,",Name)

        first, last = Name.split(" ")
        print(f"{first} let us show you our newest products")
    if New_User == "no":
        print("Thank You for checking us out!", end=" ")
        print("Goodbye.")







