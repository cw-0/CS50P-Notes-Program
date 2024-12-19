

# n = cookies

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity less than zero")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies 

    def deposit(self, n=0):
        if n < 0:
            raise ValueError("Cant deposit a negitve number of cookies")
        if self.cookies + n > self.capacity:
            raise ValueError("Cookies over capacity") 
        self.cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cant withdraw a negative number of cookies")
        if self.cookies - n < 0:
            raise ValueError("Cookies cant be less than zero") 
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


