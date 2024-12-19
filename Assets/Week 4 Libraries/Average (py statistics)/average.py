import statistics
import sys

grades = []


def main():
    while True:
        try:
            grade = float(input("Enter your grades (ctrl + d to end): "))
            grades.append(grade)
        except ValueError:
            print("Error: Number only")
            continue
        except EOFError:
            if grades:
                print(f"Your final grade is {statistics.mean(grades):.2f}" + "%")
            else:
                sys.exit("No grades entered.")
            


if __name__ == "__main__":
    main()