# P5: Use the input to find the average -

# Using the input() function, prompt the user to enter 2 numbers, and the input it taken as a string. 
# Get input from the user:
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# Using the float() function, convert the input strings to floats, now allowing us to handle decimal numbers:
number1 = float(number1)
number2 = float(number2)

# Calculate the average by adding the two numbers and dividing by 2 to get the average:
average = (number1 + number2) / 2

# Print the result
print("The average of", number1, "and", number2, "is:", average)