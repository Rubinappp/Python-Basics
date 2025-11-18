class Employee:
    raise_growth=1.04
    def __init__(self,name,income):
        self.name=name
        self.income=income
    def growth(self):
        return self.income*self.raise_growth   
    #first self will search raise_growth in its instance 
    #if it didnt found it there it will search in class employee
    #we can also write Employee.raise growth


emp1=Employee('Rubina',90000)
emp2=Employee('Prabesh',90000)

print(emp1.growth())
