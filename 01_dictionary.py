# syntax-> a={"key":"value"}
# must not have two items with same key last one will overight first one
dict= {
    "intimidate":"fill with fear" ,
   "infuriate": "to make someone extremely angry",
   "marks":[1,2,3],

   "secondict":{ 'Rubina':'beautiful'}
    }
print(dict)

# syntax: dic_name["key"]-->gives "values"
print(dict['intimidate'])
print(dict['marks'])
print(dict['secondict']['Rubina'])

# It is mutable / changeable i.e. we can add or remove 
dict['marks']=[4,10]  
dict['intimidate']="haha"
print(dict['marks'])
print(dict['intimidate'])