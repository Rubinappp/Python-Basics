#write a class calculator capable of finding square and squareroot of a number add static method to greet user with hello

class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"the value of {self.num} square is {self.num **2}")
    def cube(self):
         print(f"the value of {self.num} cube  is {self.num **3}")
    def squareRoot(self):
      print(f"the value of {self.num} cuberoot is {self.num**0.5}")  #n**0.5
    @staticmethod
    def greet():
        print("********Hello! welcome to best calculator of the world**********")
n=int(input("enter the number "))
num1=Calculator(n)
num1.square()
num1.cube()
num1.squareRoot()
num1.greet()