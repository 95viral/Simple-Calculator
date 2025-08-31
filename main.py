title = "---The Simple Calculator Using Python---"
print(title)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

try:
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        case _:
            raise ValueError("Invalid operation.")
    print(f"The result is: {result}")
except ValueError as e:
    print(e)

print("Thank you for using the calculator!")