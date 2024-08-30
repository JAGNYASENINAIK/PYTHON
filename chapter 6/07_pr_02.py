sub1=int(input("Enter first sub mark \n"))
sub2=int(input("Enter second sub mark \n"))
sub3=int(input("Enter third sub mark \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject ")

elif(sub1+sub2+sub3)/3 <40:
    print("you are failed due to total percentage is less than 40")
else:
    print("congratulations !!!! you are passed")