class Calculator:
    def __init__(self, n):
        self.n = n 
        
    def square(self):
        print(f'The square of {self.n} is : {self.n*self.n}')
        
    def cube(self):
        print(f'The cube of {self.n} is : {self.n*self.n*self.n}')
        
    def squareRoot(self):
        print(f'The square-root of {self.n} is : {self.n**1/2}')
        
        # Add a static method - 
    @staticmethod
    def greeting():
        print('Welcome to Python!')
        
# Call the methods and create the objects - 

cal = Calculator(4)

cal.greeting() # Call the static method greeting. 
cal.cube()
cal.square()
cal.squareRoot()