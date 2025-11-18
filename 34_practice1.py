#to convert celsius to fahreinheit
def farh(cel):
    return (cel*(9/5)+32)
n=int(input("enter temperature in celsius: "))
print(farh(n))