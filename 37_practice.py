#write a program to read a text from a given file poems.txt 
#and find out whether it contains the word twinkle
f=open("text.txt","r")
p=f.read()
if "twinkle" in p:
    print("twinkle is present")
else:
    print("twinkle is not present")