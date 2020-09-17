a = int(input("Side A : "))
b = int(input("Side B : "))
c = int(input("Side C : "))
if(a+b>c or a+c>b or b+c>a):
    print("Invalid Inputs, Triangle can't be formed")
else:
    if(a==b==c):
        print("It's an Equilateral Triangle")
    elif(a==b or b==c or c==a):
        print("It's a isosceles Triangle")
    else:
        print("It's a Scalene Triangle")
