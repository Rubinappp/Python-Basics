#create a class with  a class attribute a:
# create an object from it and set a directly 
#using object.a=0 does this change the class Attribute
class Sample:
    a=15
object=Sample()
object.a=0
print(Sample.a)
print(object.a)
#  Ans: NO it wont change the class attibute 