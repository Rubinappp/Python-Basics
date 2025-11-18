def max(a,b,c):
  if a>b:
     if a>c:
        return a
     else:
        return c
  else:
     if b>c:
        return b
     else:
        return c 
 

n1=int(input("enter number1 "))
n2=int(input("enter number2 "))
n3=int(input("enter number3 "))
n4=max(n1,n2,n3)
print("the largest number is "+ str(n4))
