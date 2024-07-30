""" # P12: Print a list of prime numbers from 1-100 -

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
# if the prime function is true - the prime numbers will be included in the list. """


""" def mygreeting(myName):
    print('Welcome to CBC!' + myName)
    
mygreeting()
     """
     
""" # Unknown arguments 
def student(*myStudents): # how are you able to give multiples
    print('The new student : ' + myStudents[2])
    
student('Suzanne', 'Amber', 'Salah')


def student(*myStudents): # how are you able to give multiples
    myLen = len(myStudents)
    print('The new student is now : ' + myStudents[myLen - 1])
    
student('Suzanne', 'Amber', 'Salah', 'Sadeed') """

def average():
    a = int(input('Enter your number : '))
    b = int(input('Enter your number : '))
    c = int(input('Enter your number : '))
    
    avg = (a + b + c) / 3
    print(avg)
    
average()
    

    