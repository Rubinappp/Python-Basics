a = []
for i in range(1,7):
    a.append(i)
class Trains:

    def __init__(self, name ,fare, seat):
        self.name = name
        self.fare = fare
        self.seats = seat

    def trainInfo(self):
        print(f"Train named {self.name} has {self.seats} seats with a fare price of {self.fare}.")

    def bookTicket(self):

        if self.seats > 0:
            print(f"Your ticket has been booked! Seat number is {self.seats}")
            a.remove(self.seats)
            self.seats = self.seats - 1
            

        else:
            print("No tickets available! Pls try in reservation quota.")

    def cancelTicket(self, num):
        self.num = num
        a.append(num)
        self.seats = self.seats + 1
        print(f"Your ticket has been cancelled! Seat number was {self.num}.")
        
t=Trains("Rajdhani Express","₹ 1500",6)
print(a)
t.bookTicket()
t.bookTicket()
t.bookTicket()
# i=1
# while i < 73:
#     t.bookTicket()
#     i = i+1
print(a)
t.cancelTicket(5)
print(a)
# t.cancelTicket(54)
# t.cancelTicket(44)
# t.cancelTicket(34)
# t.cancelTicket(24)
# t.cancelTicket(14)
# t.cancelTicket(4)
# t.cancelTicket(46)
# t.cancelTicket(66)
# t.cancelTicket(63)
# t.cancelTicket(12)
# t.cancelTicket(36)
# t.cancelTicket(6)
# t.cancelTicket(13)
# t.cancelTicket(55)
# t.cancelTicket(23)


# t.trainInfo() 
# print("The available seat/s no. is/are :")
# print(a)
