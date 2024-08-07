class AirTravel:
    def __init__(self, flightNo, airLine, departTime):
        self.flightNo = flightNo
        self.airLine = airLine
        self.departTime = departTime
        self.to = None
        self.fro = None
        
        # Update the class to store the travel destinations as instance variables when the booking method is called - 
    
    def booking(self, to, fro):
        self.to = to # stored instance variable 
        self.fro = fro # stored instance variable 
        print(f'Your ticket is booked in {self.flightNo} travelling from {fro} to {to}')
        
    def checkStatus(self):
        print(f'Flight number {self.flightNo} with {self.airLine} is departing at {self.departTime}')
        
        # checkFare method can use the stored destinations to print the fare - 
    def checkFare(self):
        if self.to and self.fro:
            print(f'Your fare for travelling from {self.fro} to {self.to} is $1,000' )
        else: 
            print('Please book your ticket first to check your fare.')
        
myTravelPlan = AirTravel('AC201', 'Delta', '1340')

myTravelPlan.booking('London', 'Toronto')
myTravelPlan.checkStatus()
myTravelPlan.checkFare()
# Change the above code where checkFare is not asking for to and from parameter. 