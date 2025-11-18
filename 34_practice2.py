#recursuve func to calculate sum of n natural number
# sum(n)=sum(n-1)+n

def sum(n):
  if(n==0):
    return 0
  else:
   return n+sum(n-1)
    



n=int(input("enter the number: "))
print((sum(n)))

