letter=''' Dear <|NAME|>,
you are selected as a kpop singer !!!!
date:<|DATE|>
'''
name=input("enter your name\n")
date=input("date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
