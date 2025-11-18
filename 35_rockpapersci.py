import random
def play(comp, you):
 if comp==you:
  return None
 elif comp=='r':
     if you == 's':
       return False
     else:
       return True
 if comp=='s':
     if you == 'r':
       return True
     else:
       return False
 if comp=='p':
  if  you =='r':
   return False
  else:
       return True
print("Computers turn : rock(r),scissor(s),paper(p)")
comp=random.randint(1,3)
if comp==1:
 comp='r'
elif comp==2:
  comp='s'
else:
 comp='p'
you=input("your turn : rock(r),scissor(s),paper(p):")
win=play(comp,you)
print(f"computer choose: {comp}")
print(f"You choose: {you}")
if win==True:
  print("you are winner")
elif win==None:
  print("Tie")
else:
  print("Oops you lose")


