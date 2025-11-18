class Employee:
   def __init__(self,naam,saalary):
      self.name=naam
      self.salary=saalary
   def disp(self):
      print(f"{self.name}/{self.salary}")
      
emp1=Employee("rubina",90000)
emp2=Employee("prabesh",100000)
emp1.disp()
emp2.disp()
