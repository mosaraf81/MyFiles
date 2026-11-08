# Task-1:Personal Information & Simple Calculator 

# User information:-
name = input("Enter your name: ")
age = input("Enter your age: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations:- (Fixed the 'num' typo to 'num1')
addition = int(num1 + num2)
subtraction = int(num1 - num2)
multiplication = int(num1 * num2)
division = num1 / num2

# Expected Output:-
print()  # This adds a clean empty space line
print(f"Hello, {name}!")
print(f"Your age is {age}.")
print()  # Another empty line to match the assignment layout
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")