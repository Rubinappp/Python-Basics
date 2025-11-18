#write a program to print multiplication table of given number
a=int(input("enter the number: "))

for i in range(1,11):                        #using for loop
    # print(str(a)+"x"+str(i)+"="+ str(a*i))
    print(f"{a}x{i}={a*i}") #fstring
    
#using while loop
i=0
while(i<10):
    i=i+1
    print(str(a)+"x"+str(i)+"="+ str(a*i))
     

