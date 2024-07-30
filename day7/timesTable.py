# Define the multiplier and the maximum limit:
multiplier = 2 # `multiplier`: Setting the multiplier to 2 for the 2x table.

limit = 100 # `limit`: Set the maximum limit for the times table.

# Loop from 1 to the maximum limit divided by the multiplier:
for i in range(1, limit // multiplier + 1): # iterate from 1 to the integer division of `limit` by `multiplier` plus 1 using the `range()` function.
    
    # `range()` function syntax: `range(start, stop[, step])` 
        # Used for looping a specific number of times in Python. 
        
    # THIS EXAMPLE: for i in range(1, limit // multiplier + 1)
    
    # `start`: The starting value of the sequence (inclusive) =
    # 1.
    
    # `stop`: The end value of the sequence (exclusive) =
    # `limit` is 100 and the `multiplier` is 2   r/t wanting the 2x table up to 100 -> we calculate how many multiples of 2 fit into 100
    # , limit // multiplier = integer division of 100 by 2 = 50 meaning we need 50 iterations to reach the 100 limit set in the 2x table.
    
    # `step`: The difference between each number in the sequence (optional, defaults to 1) = 
    # +1 -> gives us a needed range of 1 to 51 vs. generating numbers from 1 to 50 based on the `, limit // multiplier` calculation. By adding the +1 we make sure to include 50  r/t the loop including the highest multiple of 2 that fits within the limit of 100. 
        # For example: `range(1, limit // multiplier +1)` becomes `range(1, 51)`
        
# Without the +1:   for i in range(1, 50):  # This will generate numbers 1 to 49
                  # result = 2 * i
                  # print(f"2 x {i} = {result}") # Output will stop at 2 x 49 = 98
    
    result = multiplier * i # Calculate the product of the multiplier and the current value of `i`.
    
    print(f"{multiplier} x {i} = {result}") # Print the multiplication statement using the f string to format strings in Python. 
    
    
    for y in range(1,11):
        print(f'2 * {y} = {2*y}')

# Nesting
for x in range(2,6 + 1):
    for y in range(1,11):
        print(f'{x} * {y} = {x*y}')
        
for a in range(6):
    print(a) # Output - 0 1 2 3 4 5
    
for b in range(1,6):
    print(b) # Output - 1 2 3 4 5
    
myList = [50, 63, 85, 15]
for x in myList:
    print(x)
    
myList = 'Welcome to CBC!'
for x in myList:
    print(x)
    
myList = [5, 10, 6, 4]
for x in myList:
    print(x)
else:
    print('completed Printing')
    
