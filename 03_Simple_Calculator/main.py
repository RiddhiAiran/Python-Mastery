# Simple Calculator
# Description: This program performs basic arithmetic operations (addition, subtraction, multiplication, division, modulus, exponentiation, and floor division) on two numbers provided by the user.

# Step 1: Take User Input for Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform Basic Arithmetic Operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined (cannot divide by zero)"
exponentiation = num1 ** num2
floor_division = num1 // num2 if num2 != 0 else "undefined (cannot divide by zero)"

# Step 3: Display the Results
print("\n 🙏🏼-----Simple Calculator----- 🙏🏼\n")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print("\nThank you for using the Simple Calculator! 🙏🏼\n" )