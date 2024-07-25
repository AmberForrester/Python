# P4: Use the input to add two numbers, using the `input()` function to get user input and then convert the input to integers (or floats) before adding them - 

"""
num1 = input('Enter the value for num1: ')

print(type(num1))

"""

# Using the input() function, prompt the user to enter 2 numbers, and the input it taken as a string. 
# Get input from the user:
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# Using the int() function, convert the input strings to integers:
number1 = int(number1)
number2 = int(number2)

# Add the numbers using the + operater and store the result in the variable `result`:
result = number1 + number2

# Print the result using the print() function:
print("The sum of", number1, "and", number2, "is:", result)