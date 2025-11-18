
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+last+'@gmail.com'
   
# emp_str1='john-Doe-7000'
# emp_str2='prativa-gautam-100000'
# emp_str3='Rubina-Poudel-70000'
# first,last,pay=emp_str1.split('-')
# new_emp1=Employee(first,last,pay)
# print(new_emp1.first)
#inspite ofsplitting every string to create a new employee we can create alternative constructorthat splits string and create employee 

#using class method as alternative constructor
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@gmail.com'
    @classmethod
    def from_string(cls,emp_str): #alternatiev constructor
        first,last,pay=emp_str.split('-')#splits the string 
        return cls(first,last,pay) #this will create new employee object and return
   
emp_str1='john-Doe-7000'
emp_str2='prativa-gautam-100000'
emp_str3='Rubina-Poudel-70000'

new_emp1=Employee.from_string(emp_str1)


print(new_emp1.first)
print(new_emp1.email)
print(new_emp1.last)
