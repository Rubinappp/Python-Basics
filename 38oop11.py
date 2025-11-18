class Employee:
    company="google"
    def getSalary(self):
        print(f"salary for employee working in {self.company }is {self.salary}")
Rubina=Employee()
Rubina.salary=100000
Rubina.getSalary()#equivalent to Employee.getSalary(Rubina)
#the above sentence is converted into this

