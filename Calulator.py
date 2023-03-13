from math import *
# Symbols of operations: + -- Addition - -- Subtraction * -- Multiplication / -- Division ^ -- Exponentiation log -- Logarithm
print("Welcome to Kirako's Calculator, "
      "Current version: 1.2")
operation = input("Enter the symbol of which operation do you want to do: ")

if operation == "+":  # Addition
    num1 = input("First number: ")
    num2 = input("Second number: ")

    print((float(num1)) + (float(num2)))
elif:
    operation == "-":  # Subtraction
        num1 = input("First number: ")
        num2 = input("Second number: ")

        print((float(num1)) - (float(num2)))
    elif:
        operation == "*":  # Multiplication
            num1 = input("First number: ")
            num2 = input("Second number: ")

            print((float(num1)) * (float(num2)))
        elif:
            operation == "^":  # Exponentiation
                num1 = input("First number: ")
                num2 = input("Second number: ")
                print(pow((float(num1)), (float(num2))))
            elif:
                operation == "log":  # Logarithm
                    num1 = input("First number: ")
                    num2 = input("Second number: ")
                    print(log(float(num1), (float(num2))))
                elif:
                    operation == "/":  # Division pt.1
                        num1 = input("First number: ")
                        num2 = input("Second number: ")
                        if num2 == "0":  # Division by 0
                            print("Error")
                        else:  # Division pt.2
                            print((float(num1)) / (float(num2)))
