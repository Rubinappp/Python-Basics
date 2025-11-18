#write a program to print the following star pattern
#      *
#     * *
#    * * *
#   * * * *
for i in range(4) :
     print(" "* int(4-i-1),end="")
     for j in range(i+1):
       print("*",end="")
       print(" ",end="")

     print()