class Employee:
    company="Google"
    def showDetails(self):
        print("This is an employee")
class Programmer(Employee):
    language="Python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):  #method overriding
        
        print("This is an employee1")
obj=Programmer()
print(obj.company)
obj.getLanguage()
obj.showDetails()
Employee.showDetails(obj)

