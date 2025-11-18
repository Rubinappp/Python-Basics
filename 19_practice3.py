sub1=int(input("enter marks ofsub1"))
sub2=int(input("enter marks of  sub2"))
sub3=int(input("enter marks of sub3"))
p=(sub1+sub2+sub3)/3
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail becuase you have more than 33 percent in one of the subject")
elif(p>=40):
   print("you are pass")
else:
    print("you are fail because your total percentage is less than 40")




