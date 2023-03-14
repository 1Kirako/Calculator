from math import *
# Symbols of operations: + -- Addition - -- Subtraction * -- Multiplication / -- Division ^ -- Exponentiation log -- Logarithm
print("Welcome to Kirako's Calculator, ")
print("Current version: 2.1")
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
elif operation == "/":  # Division pt.1
                        num1 = float(input("First number: "))
                        num2 = float(input("Second number: "))
                        if num2 == "0":  # Division by 0
                            print("Error")
                        else:  # Division pt.2
                            print(num1 / num2)
