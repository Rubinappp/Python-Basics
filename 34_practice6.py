#write a function to remove a given word from a list and strip at the same time
#strip will remove extra space 
def remove_strip(string , word):
    newstr=string.replace(word ,"")
    return newstr.strip()

this="  i am very beautiful  "
print(remove_strip(this , "very"))
