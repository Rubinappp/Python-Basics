class Person:
    country="Nepal"
    def takeBreath(self):
        print("i am breathing")
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        print('I AM ALSO BREATHING')
class Programmer(Employee):
    company="Fiverr"
    def getSalary(self):
        print("no salary to programmers")
p=Person()
e=Employee()
pr=Programmer()


