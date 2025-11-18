class Employee:
    company="Nepal Gas"
    salary=5600
    salaryBonous=400
    #totalSalary=6000
    @property
    def totalSalary(self):
      return self.salary+self.salaryBonous
e=Employee()
print(e.totalSalary)