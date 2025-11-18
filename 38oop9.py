#class variable /Attribute
#they belongs to class rather than object 
class Employee:
    company='GOOGLE'    
Rubina=Employee()
Prativa=Employee()
print(Rubina.company)
print(Prativa.company)
Employee.company='YOUTUBE'
print(Rubina.company)
print(Prativa.company)