import os
import sys

class Student:
    def __init__(self, name, house):
        self.name = name.title()
        self.house = house.title()
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter (Name)
    @property
    def name(self):
        return self._name
    
    # Setter (Name)
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter (House)
    @property
    def house(self):
        return self._house
    
    # Setter (House)
    @house.setter
    def house(self, house):
        if house.title() not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house    



def main():
    student = get_student()
    #student.house = "This will raise Value Error due to getter and Setter"
    print(student)




def get_student():
    while True:
        try:
            name = input("Name: ").strip()
            house = input("House: ").strip()
            return Student(name, house)
        except ValueError as e:
            print(f"Error: {e}")
            input("Press Enter to try again")
            clear_console()
            continue



def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



if __name__ == "__main__":
    main()