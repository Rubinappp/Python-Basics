# super()method
class Person:
    def __init__(self) :
       print("Person class")
       
    def takeBreath(self):
        print("i am breathing")

class Employee(Person):
    def __init__(self) :
       super().__init__()
       print("Employee class")

    def takeBreath(self):
        super().takeBreath()
        print('I AM ALSO BREATHING')

class Programmer(Employee):
    def __init__(self) :
       super().__init__()
       print("Programmer class")

    def takeBreath(self):
        super().takeBreath()
        print('I AM BREATHING++')


pr=Programmer()
pr.takeBreath()
