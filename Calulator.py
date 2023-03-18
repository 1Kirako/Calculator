from math import *
# Symbols of standard calculator operations: + -- Addition - -- Subtraction * -- Multiplication / -- Division
# Symbols of other operations ^ -- Exponentiation log -- Logarithm sqrt - Square root
# Welcome to the Calculator
# Current version: 3.0
operation = input("Enter the symbol of which operation do you want to do: ")
if operation == "+":  # Addition
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(num1 + num2)
elif operation == "-":  # Subtraction
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(num1 - num2)
elif operation == "*":  # Multiplication
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(num1 * num2)
elif operation == "^":  # Exponentiation
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(pow(num1, num2))
elif operation == "log":  # Logarithm
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print(log(num1, num2))
elif operation == "sqrt":  # Square root
    num1 =float(input("Number: "))
    print(sqrt(num1))
elif operation == "/":  # Division pt.1
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    if num2 == "0":  # Division by 0
        print("Error")
    else:  # Division pt.2
        print(num1 / num2)
