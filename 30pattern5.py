# print this pattern
#      *
#     * * 
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

for i in range(6):
    print(" " * int(6-i-1),end="")
    for j in range(i+1):
      print("*",end="")
      print(" ",end="")
    print()
