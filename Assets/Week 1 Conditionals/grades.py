score = float(input("Score: "))

if score >= 90:
    print("You got an A!")
elif score >=80 and score < 90:
    print("You got a B!")
elif score >= 70 and score < 80:
    print("You got a C")
elif score >= 60 and score < 70:
    print("You got a D")
elif score >= 0 and score < 60:
    print("You got an F :/")
else:
    print("invalid number")