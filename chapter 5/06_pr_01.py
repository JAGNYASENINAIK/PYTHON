hindi={"pankha":"fan","ghadi":"watch","pani":"water","mandir":"temple"}
# print(hindi["pankha"])
# print(hindi["pani"])

print("options are:",hindi.keys())
a=input("enter the hindi word :")
# print("the meaning of the word :",hindi[a]) # it will throw error if key is not present
print("the meaning of the word :",hindi.get(a)) # this wont throw errorpr