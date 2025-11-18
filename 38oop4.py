class Employee:
    raise_growth=1.04
    def __init__(self,name,income):
        self.name=name
        self.income=income
    def growth(self):
        return self.income*self.raise_growth  


emp1=Employee('Rubina',90000)
emp2=Employee('Prabesh',90000)
#print(emp1.__dict__)
# print(Employee.__dict__)
emp1.raise_growth=1.05
print(emp1.growth())
print(emp2.growth())
