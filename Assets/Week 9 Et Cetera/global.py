class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        print(f"* Deposited ${n}")
        self._balance += n

    def withdraw(self, n):
        print(f"* Withdrew ${n}")
        self._balance -= n



def main():
    account = Account()
    print(f"Starting Balance: ${account.balance}\n")
    account.deposit(100)
    account.withdraw(50)
    print(f"\nNew Balance: ${account.balance}")





if __name__ == "__main__":
    main()