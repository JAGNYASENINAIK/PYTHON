# marks=[56,78,98,33]
# percentage1=(sum(marks)/400)*100
# marks2=[78,23,48,33]
# percentage2=(sum(marks2)/400)*100
# print(percentage1,percentage2)
# percentage1=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# print(percentage1)

def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[56,78,98,33]
percentage1=percent(marks1)

marks2=[78,23,48,33]
percentage2=percent(marks2)
print(percentage1,percentage2)





