# P13. Create a function to do adding, subtracting, and dividing two numbers -



# Define function - calculate that takes 3 arguments: operation, x, y -
def calculate(operation, x, y):
    
    # Define a dictionary {using curly braces}, that maps operation names as strings to lambda functions that match math operations - 
    operations = {
        
        # Define three key : value pairs in the operations dictionary -
        'add': lambda a, b: a + b, # add maps to a lambda function that takes 2 arguments and returns their sum. 
        
        'subtract': lambda a, b: a - b, # subtract maps to a lambda function that takes 2 arguments and returns their difference. 
        
        'divide': lambda a, b: a / b if b != 0 else 'Division by zero error' # division maps to a lambda function that takes 2 arguments and returns their quotient if 1 argument is not 0; otherwise it will return the string error message. 
    }
    
    # Argument operation is used to look up matching lambda function in the operations dictionary, calling the lambda function with x,y arguments to return the result -
    return operations[operation](x, y)

# Call the calculate function defined with different operations, each looking up to the lamda function to match the math operation - 
print(calculate('add', 10, 5))        # Output = 15
print(calculate('subtract', 10, 5))   # Output = 5
print(calculate('divide', 10, 5))     # Output = 2.0
print(calculate('divide', 10, 0))     # Output = Division by zero error