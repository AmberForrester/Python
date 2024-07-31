# P14. Find the factorial of any number/input -


# Define function - factorial that takes 1 parameter: n  -  
def factorial(n):
    
    # Single line conditional statement = Ternary Operator: 
        # check if n is 0 = return 1 R/T the factorial of 0 is 1
        # if n is NOT 0 = return n multiplied by result of factorial(n-1)
    return 1 if n == 0 else n * factorial(n - 1)

# Call the factorial function with preferred arguments 
print(factorial(5)) # Output = 120 - 5 x 4 x 3 x 2 x 1 
print(factorial(0)) # Output = 1 - 0 = 1 
print(factorial(7)) # Output - 5040 - 7 x 6 x 5 x 4 x 3 x 2 x 1 