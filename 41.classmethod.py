#if we want to change class attribute not change or add instance attribute we use class method
class Employee:
    company="camel"
    salary=100
    location="Delhi"
    #it is the one of the method to change class attribute
    # def changeSalary(self,sal):
    #     self.__class__.salary=sal
    
    @classmethod
    def changeSalary(cls,sal):
     cls.salary=sal
e=Employee()
print(Employee.salary)
e.changeSalary(150)
print(Employee.salary)