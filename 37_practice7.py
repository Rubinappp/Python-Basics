# write a program to find out whether file is identical and makes the content of another file
with open ("copy.txt") as f:
    content=f.read()
with open("this.txt")as f:
    contents=f.read()
if (content==contents):
    print("yes they are identical")
else:
    print("no they are not identical")