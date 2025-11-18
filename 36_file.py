# opening a File
# open("this.txt","r") open()function take two parameter file name and mode of opening
f = open('sample.txt')#by default mode is r
# data=f.read(7)it will read 7 character
data=f.read()
print(data)
f.close()