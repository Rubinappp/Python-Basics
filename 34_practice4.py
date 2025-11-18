#using only i
n=5
for i in range(n):
    print("*" * (n-i))

#using i and j
for i in range(6):
  for  j in range(6-i):
     print("*",end="")
  print()