f=open("sample.txt",'r')
data=f.readline()      # read first line
print(data)
data=f.readline()   # read second line
print(data)
f.close()