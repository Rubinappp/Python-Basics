#static method

class Employee:
    company="google"
    def getSalary(self,signature):
        print(f"salary for employee working in {self.company }is {self.salary}\n{signature}")
   
    #static method is used when there is no use of self /instance so passing instance become worthless.. static wont take any argument
      #it is decorater
    @staticmethod
    def greet():
        print("hello sir")

Rubina=Employee()
Rubina.salary=100000

Rubina.getSalary("Thanks!")#equivalent to Employee.getSalary(Rubina)
#the above sentence is converted into this

