import os
import sys

class Student:
    def __init__(self, name, house):
        self.name = name.title()
        self.house = house.title()
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        while True:
            try:
                name = input("Name: ").strip()
                house = input("House: ").strip()
                return cls(name, house)
            except ValueError as e:
                print(f"Error: {e}")
                input("Press Enter to try again")
                clear_console()
                continue



def main():
    student = Student.get()
    print(student)







def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



if __name__ == "__main__":
    main()