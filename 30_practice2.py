a=int(input("enter the number"))
# k=0

# for i in range(2,a):
#    if(a%i==0):
#     k=k+1
   
# if k>0:
#   print("the number is not prime")
# else:
#   print("the number is prime")

prime=True
for i in range(2,a):
   if(a%2==0):
    prime=False
    break
if prime:
  print("this number is prime")
else:
  print("this number is not prime")
  
  