#instance attribute
#attribute that belongs to instance

class Employee:
    salary=10000 #creating class attribute
    company='GOOGLE'    
Rubina=Employee()
Prabesh=Employee()
#creating instance attribute salary for both objects it wont change class attribute rther it will add instance attribute
Rubina.salary=100000
Prabesh.salary=200000

print(Rubina.salary)
print(Prabesh.salary)
