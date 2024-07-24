# Arithmetic Operators
a = 10
b = 20 
print (a + b)

x = 10
y = 20
z = x + y
result = x + y
print(result)

# Assignment Operator 
a = 6+3
print(a)
b = 10

b -= 6 # or b = b - 6
print(b)

b += 3 # or b = b + 4
print(b)

# Comparison Operator: it compares two values on the L + R side
name = "F"
flag = name == "F"
print(flag)

# Logical Operators 

# Operators = and + or: if we have values that are getting compared using and/or in between we will get true or false based on HOW they are compared using the Logical Operators - 
# and
# or 

num1 = 1
num2 = 2

print(num1 or num2)
print(num1 and num2)


# Truth Table - 
# Using the or Operator: If any one of the conditions are true = true 
print(True or False) # True
print(False or True) # True
print(True or True) # True
print(False or False) # False

# Using the and Operator: If any one of the conditions are false = false 
print(True and False) # False
print(False and True) # False
print(True and True) # True
print(False and False) # False


num1 = 10
num2 = 10
x = "A"
y = "A"

print(num1 == num2) # True
print (x == y) # False

check = num1 == num2 or x == y
print(check) # True

check = num1 == num2 and x == y
print(check) #False

