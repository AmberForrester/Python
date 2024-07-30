""" myList = 1
while myList < 10:
    print(myList)
    myList += 1 # Without this line, you will have an infinite output because it has nothing to compare to. 
    
i = 1
while i < 6:
    print(i)
    if i == 3: # Give the loop a control statement.
        break  # A loop without a control statement = infinite loop.
    i += 1 """
    
""" i = 1
while i < 6:
    print(i)
    if i == 3: # Give the loop a control statement.
        break  # A loop without a control statement = infinite loop.
    i += 2  # 1 + 2 = 3 """
    
""" students = ['Amber', 'Suzanne', 'Salah', 'Syed', 'Suze', 'Johnathan']
i = 2
while i < len(students):
    print(students[i])
    i += 1
    
for i in range(100 + 1):
    if i == 34:
        break
    print(i)
    
for i in range(100 + 1):
    if i == 34:
        continue
    print(i) """
    
""" # P10: From a list of student print all the names starting with "S" -
students = ['Amber', 'Suzanne', 'Salah', 'Syed', 'Suze', 'Johnathan']
for student in students: 
    if student.lower().startswith('s'):
        print(student) """
        
""" # P11: Take an input from the user, for the same input generate the table ( 2 * 1 = 2) using while loop -
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f'{num} * {i} = {num * i}')
    # i += 1
    break
    # i += 1
     """

# P12: Print a list of prime numbers from 1-100 -

def prime(n): # define the function named prime.
              # parameter n - represent the prime number.
              
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# n > 1 = Check if number is > 1 r/t Prime Numbers = > 1.

# and = Logical Operator making n > 1 and all conditions must be true for the entire expression to return true.
# all = will check if n is NOT divisible by any number from 1 - 100, making sure the definition of a Prime Number is followed.

# n % i = checks if n is divisible by i.
# n ** 0.5 = calculates the sqaure root of n.

print([num for num in range(2, 101) if prime(num)]) # List Comprehension 

# iterates to find the Prime Numbers.
# checks conditions by calling the prime function defined above
# if the prime function is true - the prime numbers will be included in the list.
