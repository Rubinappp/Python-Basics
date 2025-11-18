class Employee:
    company="visa"
class Freelancer:
    company="Fiver"
class Programmer(Employee,Freelancer):
    name="Rubina"
p=Programmer()
print(p.company) #employyee is inherited first so visa is printed