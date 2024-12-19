expression = (input("Expression: "))

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

add = x + z
subtract = x - z
multiply = x * z
divide = x / z

if y == "+":
    (print(f"Answer: {add:.1f}"))
elif y == "-":
    (print(f"Answer: {subtract:.1f}"))
elif y == "*":
    (print(f"Answer: {multiply:.1f}"))
elif y == "/":
    (print(f"Answer: {divide:.1f}"))
else:
    print("Unknown expression. Please use +, -, *, or / with spaces")