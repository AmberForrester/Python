# When we declare a class, and declaring the methods. 
# We need a way to initialize those attributes. 

# Construtor is a special type of method, that allows us to assign the initial values of our attributes. 

class Employee:
    department = 'IT Services'
    salary = '230000K per year'
    
    # two values are department and salary. 

# When I am declaring an object, and call the name of employee etc. 

def greetings(msg):
        print(f'Hello, have a nice day.\n Your department is: {msg.department}\n Your starting salary is: {msg.salary}')

FSD1 = Employee('Amber', 230000, 'API connections')

print(FSD1.msg)