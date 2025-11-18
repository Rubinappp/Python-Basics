class employee:
   def display(self):
      print(f"{self.name}/{self.salary}")
      
emp1=employee()
emp2=employee()
emp1.name="rubina"
emp2.name="prativa"
emp1.salary=90000
emp2.salary=100000
emp1.display()
emp2.display()
