myDict= {
    "intimidate":"fill with fear" ,
   "infuriate": "to make someone extremely angry",
   "marks":[1,2,3],
   "secondict":{ 'Rubina':'beautiful'},
   1:2
   }
#dictionary methods
print(myDict.keys()) #print keys of dictionary
print(myDict.values()) #print values of dictionary
print(myDict.items()) #print (keys,value) for all contents of the dictionary
print(myDict)

#updating dictionary adding more keys and values 
updateDict={"color":"green",
            "food":"momo"}
myDict.update(updateDict) 
print(myDict)


print(myDict.get("color")) #print values and return none if key is not present
print(myDict["color"])  #print values and if key is not present throws error