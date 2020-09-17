num = float(input("Number : "))
sqroot = num**(0.5)
print(sqroot)
flag=0
sqroot=int(sqroot)
if sqroot==1 or sqroot==0:
    print("Neither prime nor composite")
else:
    for i in range(1,sqroot+1):
        if(sqroot%i==0):
            flag=flag+1
    if flag==2:
        print("Prime Number ")
    else:
        print("Not a prime number")