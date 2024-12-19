print("Change Accpeted: Quarters, Nickels, Dimes.")

amount = 50

while amount > 0:
        print(f"Amount Due: {amount}")
        insert = int(input("Insert Coin: "))
        if insert in [5, 10, 25]:
            amount -= insert
        else:
            continue

amount = amount - 0
print(f"Change Owed: {abs(amount)}")