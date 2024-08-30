#Creating an empty set   unordered, unindexed,no duplicate
g=set()
print(type(g))
#Adding values to an empty set
g.add(7)
g.add(89)
g.add(9)
g.add(34)
g.add(7) # adding a value repeatedly doen not change the set
# g.add([4,5,6]) #list can't be added in the set as list can be changed later ( not hashable)
  
 #accessing elements 
g.add((4,5,6))  #can add tuples 
# g.add({"def":"efg"}) # dict can not be addeed
print(g)
# in sets we can only add element which can not be changed later (only unique value)

#length of set
print(len(g))
#removal of an item
g.remove(34)
# g.remove(90)  #throws an error
print(g)
print(g.pop())
print(g)
