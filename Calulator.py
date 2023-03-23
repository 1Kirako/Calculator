from math import *
# Symbols of standard calculator operations: + -- Addition - -- Subtraction * -- Multiplication / -- Division
# Symbols of other operations ^ -- Exponentiation log -- Logarithm // - Square root
# Welcome to the Calculator
# Current version: 4.2
operation = input("Enter the symbol of which operation do you want to do: ")
if operation == "//":  # Square root
    num1 = float(input("Number: "))
    print(sqrt(num1))
else:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    if operation == "+":  # Addition
        print(num1 + num2)
    if operation == "-":  # Subtraction
        print(num1 - num2)
    if operation == "*":  # Multiplication
        print(num1 * num2)
    if operation == "^":  # Exponentiation
        print(pow(num1, num2))
    if operation == "log":  # Logarithms
        print(log(num1, num2))
    if operation == "/":  # Division
        if num2 == 0:
            print("Error!")
        else:
            print(num1 / num2)
            
