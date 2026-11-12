
# Question 6: Function-Based Calculator

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")

if operation == "+":
    print("Result:", addition(num1, num2))

elif operation == "-":
    print("Result:", subtraction(num1, num2))

elif operation == "*":
    print("Result:", multiplication(num1, num2))

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", division(num1, num2))

else:
    print("Invalid operation.")
