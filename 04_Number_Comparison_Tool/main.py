# Number Comparison Tool
# Description: This program compares two numbers and provides feedback on their relationship.


print("\n 🙏🏼-----Number Comparison----- 🙏🏼\n")

# Step 1: Take User Input for Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Compare the Numbers
print("\n -----Comparison Result----- \n")
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num2} is greater than {num1}.")
elif num1 == num2:
    print(f"{num1} is equal to {num2}.")
else:
    print("Invalid input. Please enter valid numbers.")

# Step 3: Check if any number is zero
if num1 == 0 and num2 == 0:
    print("Both numbers are zero.")
elif num1 == 0 or num2 == 0:
    print("\nOne of the numbers is zero.\n")
else:
    print("\nBoth numbers are non-zero.\n")