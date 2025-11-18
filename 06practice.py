#write a program to create a dictionary of nepali words with values as their english translation 
dict={
    "dhoka":"door",
    "jhyal":"window"
}

p=(dict[input("enter the nepali word\n")])       #will show error when we give name not present in dictionary
print(p)
q=input("enter the nepali word\n")
print("the meaning of nepali word is",dict[q]) #will show error when we give name not present in dictionary

#will not throw error if key is not present
z=input("enter key:")
print ("meaning of word",z,"is",dict.get(z))