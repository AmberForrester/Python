""" myString = "You are an amazing Full Stack Developer"
print(len(myString)) """


# Dynamic or Run-Time Polymorphism 
# Overriding 
# Multiple Classes with the same method name - 

# Giving the Car, Boat, Plane all the same move method but with it's own implementation. 

class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print('My car is now moving!')
        
class Boat: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print('My boat is sailing!')
        
class Plane: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print('My plane is flying!')
        
car1 = Car('BMW', 'X5M') # Create a Car class 
boat1 = Boat('Bayliner', 'Trophy T25 Pilothouse') # Create a Boat class 
plane1 = Plane('Boeing', '1250') # Create a Plane class 

for x in (car1, boat1, plane1):
    x.move()