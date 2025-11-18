# A spam text contains following "make a lot of money","buy now",
#"subscribe this","click this",write a program to detect these spams
text = input("enter the text\n")
if("make a lot of money"in text):
    spam = True
elif("buy now"in text):
   spam=True
elif("watch this "in text):
   spam=True
elif("subscribe this"in text):
   spam=True
else:
   spam=False
if(spam):
  print("this text is spam")
else:
   print("this text is not spam")
