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

