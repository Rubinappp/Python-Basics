# PROJECT1:
import random
def gamewin(comp,you):
 if comp==you:
   return None
 elif comp=='s':
     if you=='w':
       return False
     else:
       return True
 elif comp=='w':
      if you=='s':
         return True
      else:
         return False
 else :
    if comp=="g":
     if you=="w":
       return True
     else:
       return False
print("computers turn : snake(s),water(w),gun(g)")
randomnum=random.randint(1,3)

if (randomnum==1):
  comp='s'
elif (randomnum==2):
  comp='w'
else:
  comp='g'
you=input('your turn snake(s),water(w),gun(s):')
win=gamewin(comp,you)
print(f"computer choose: {comp}")
print(f"you choose: {you}")
if (win==None):
  print('Tie')
elif(win==True):
  print("congratulation!you are winner")
else:
  print("Oops you lose!")