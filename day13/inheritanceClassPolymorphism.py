class Transportation: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print('Move!')

class Car(Transportation):
    pass
        
class Boat(Transportation): 
    def move(self):
        print('Sail!')
    
class Plane(Transportation): 
    def move(self):
        print('Fly!')
        
car1 = Car('BMW', 'X5M') # Create a Car class 
boat1 = Boat('Bayliner', 'Trophy T25 Pilothouse') # Create a Boat class 
plane1 = Plane('Boeing', '1250') # Create a Plane class 

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()