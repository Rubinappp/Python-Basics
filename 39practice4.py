#write a class Train which has methods to book a ticket get status (no of seats )and get fare information of trains running under Indian Railways
a=[]
for i in range(1,11):
      a.append(i)
class Train:
   
    def __init__(self,name,fare,seats) :
      self.name=name
      self.fare=fare
      self.seats=seats
  
   
    def getStatus(self):
        print("***************")
        print(f"the name of the train is {self.name}")
        print(f"the seats available in the train is {self.seats}")
        print("***************")
    def Book(self):
      if(self.seats>0):
         print(f"your ticket is booked.your seat number is {self.seats}")
         self.seats-=1
      else:
         print("Sorry this train is full")
    def fareInfo(self):  
        print(f"the price of ticket is Rs.{self.fare}")
    def cancelTicket(self,seatno):
       print(f"Your seat number {seatno} is canceled")
       a.append(seatno)
       self.seats=self.seats+1


Intercity=Train("Intercity Express:1405",90,10)
Intercity.getStatus()
Intercity.Book()
Intercity.getStatus()
Intercity.Book()
Intercity.fareInfo()
Intercity.cancelTicket(9)
Intercity.getStatus()