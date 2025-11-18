# using function
def percent(marks):
    p=(marks[0]+marks[1]+marks[2]+marks[3])/400*100
    return p
marks1=[21,33,53,53]
marks2=[20,3,53,23]
percentage1=percent(marks1)
percentage2=percent(marks2)
print(percentage1,percentage2)