#write a program to find out if address is present or not and the line number where address is present in logfile.txt
content=True
i=0
with open("logfile.txt")as f:
    
    while content:
      i+=1
      content=f.readline()
     

      if 'address' in content :
          print(content)
          print("yes address is present")
          print(i)
      