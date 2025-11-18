#constructor
# __init__ is the special method which is first run as soo ans object is created
#it is called constructor as it helps to initialize object
# It takes self argument and can also take further arguments.
class Employee:
    company="google"
    
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
      
    def getDetails(self):
        print(f"salary for {self.name} working in {self.subunit} is {self.salary}")

Rubina=Employee("Rubina",100000,"youtube")
Rubina.getDetails()