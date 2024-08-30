myDict={
 "reenu":"a student",
 "BTS": "biggest boy band",
 "marks" :[1,6,9],
 "adict":{"su":" a coder"},
 1:4
}
#dictionary methods
print(myDict.keys()) # prints the keys of the dictionary
print(type(myDict.keys())) # prints the type of dict (this is type)
print(list(myDict.keys())) 
'''prints the keys of dict(this is type casting/converting to
 list'''
print(myDict.values())
print(myDict.items())
print(myDict)
updateddict={"lovish":"friend","kill":"death","reenu":"a girl"}
myDict.update(updateddict)
'''update the dictionary by adding the key values pairs 
from updateddict'''
print(myDict)

# THE DIFFERENCE BETWEEN .get and []syntax in dictionaries ???//
print(myDict.get("reenu")) #prints value associated with key reenu
print(myDict["reenu"])  

print(myDict.get("reenu8")) # returns NONE as reenu8 is not present 
print(myDict["reenu8"])#throws an error as reenu8 is not present in the dictionary