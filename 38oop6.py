#difference between regular method,class method and static method
#in regular method instance varibale self is our first argument 
#in class method class variable cls is our first argument class method automaticlly pass cls as first argument
#staticmethod dont take instance or class as first argument
class Employee:
    raise_growth=1.04


    def __init__(self,name,income):
        self.name=name
        self.income=income
        Employee.num_of_emp+=1  #it will change every time init function gets called work same as static variable in c++ .        
    def growth(self):
        return self.income*self.raise_growth  

    @classmethod
    def set_amount(cls,amount): #we can directly write employee.raisegrowth(1.05) to change class variable but inspite of that we are using class method to do that
      cls.raise_growth=amount

emp1=Employee('Rubina',90000)
emp2=Employee('Prativa',90000)

Employee.set_amount(1.05)#emp1.set_amount(1.05) this will also change class variable

print(emp1.raise_growth)
print(emp2.raise_growth)
print(Employee.raise_growth)

