#create a class programmer for string information of the programmers working at microsoft 
class Programmer:
    company="Microsoft"
    def __init__(self,name,product) :
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"the name of the programmer is {self.name} and the product is {self.product}")
Rubina=Programmer("Rubina","skype")
Prabesh=Programmer("Prabesh","GitHub")
Rubina.getInfo()
Prabesh.getInfo()
