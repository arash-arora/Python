rad = float(input("Radius : "))
ch = input("1. Area\n2. Perimeter ")
if(ch=='1'):
    area=3.14*rad*rad
    print("Area :",area)
elif(ch=='2'):
    per=2*3.14*rad
    print("Perimeter :",per)
else:
    print("Invalid!")