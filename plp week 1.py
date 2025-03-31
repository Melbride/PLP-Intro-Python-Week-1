#A python program that asks the user to input two numbers and a mathematical operation is performed based on the user's input and print the result.

num1 = float(input('Enter the first number'))
num2 = float(input('Enter the second number'))
operation = input("Enter an operation (+, -, *, /):")

if operation == "+":   
    result = num1 + num2
    
elif operation == "-":
    result = num1 - num2
    
elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 == 0:
        result = "Error: Division by zero is no allowed."
    else:
        result = num1 + num2    
else:
    result = "Not the right operation"

print(f"{num1} {operation} {num2} = {result}")
