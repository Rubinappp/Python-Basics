#write a program to calculate factorial of a given number using for loop
factorial=1
b=int(input("enter number"))
for i in range(1,b+1):
    factorial=factorial*i
print(f"factorial is: {factorial}")

