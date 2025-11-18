#class variable /Attribute
#they belongs to class rather than object 
class Employee:
    company='GOOGLE'    
Rubina=Employee()
Prabesh=Employee()
print(Rubina.company)
print(Prabesh.company)
Employee.company='YOUTUBE'
print(Rubina.company)
print(Prabesh.company)