class Employee:
    raise_growth=1.04
    num_of_emp=0

    def __init__(self,name,income):
        self.name=name
        self.income=income
        Employee.num_of_emp+=1  #it will change every time init function gets called work same as static variable in c++ .        
    def growth(self):
        return self.income*self.raise_growth  


emp1=Employee('Rubina',90000)
emp2=Employee('Prabesh',90000)
emp1.raise_growth=1.05

print(emp1.raise_growth)
print(emp2.raise_growth)
print(Employee.raise_growth)

print(Employee.num_of_emp)
