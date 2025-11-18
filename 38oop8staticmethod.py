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
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_str1='john-Doe-7000'
emp_str2='prativa-gautam-100000'
emp_str3='Miss-Rubina-70000'
import datetime
my_date=datetime.date(2023,6,11)
print(Employee.is_workday(my_date))