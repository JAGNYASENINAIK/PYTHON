# # Concatenating two string
greeting="good evening,"   
name="reenu"
print(type(name))
c=greeting+name
print(c)

# # Slicing
name="REENU"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# #  name[3]="y"  -->doesn't work

# print(name[0:5])
# print(name[2:5])

# print(name[:4]) # is same as [0:4]
# print(name[1:])# is same as [1:5]
# c=name[-4:-1] #[1:4]
# print(c)

# slicing with skip  value
name="RenuIsGood"
d=name[3:6:2]
d=name[3:8:2]
d=name[0:8:2]
# d=name[0:8:5]
print(d)
word='amazing'
k=word[1:6:2]
print(k)

