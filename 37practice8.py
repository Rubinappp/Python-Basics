#wite a program to rename a file to removed.txt
import os
with open("jdfdk.txt")as f:
    content=f.read()
os.remove("jdfdk.txt")
with open("removed.txt","w")as f:
   f.write(content)