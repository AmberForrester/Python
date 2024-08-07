class Employee:
    department = 'IT Services'
    salary = '230000K per year'
    
    
    def __init__(self, fname, department, salary):
        self.department = department
        self.salary = salary
        self.fname = fname

    def greetings(self):
        print(
            f"Hello {self.fname}, have a nice day.\n Your Department is : {self.department}\n Your base salary is : {self.salary}"
        )
        
abc = Employee('Amber', 'IT Services', '350000k per year')
abc.greetings()
