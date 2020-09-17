num = (input("Number : "))
res=0
l=len(num)
#print(l)
num=int(num)
numb = num
while(num!=0):
    rem=num%10
    num=num//10
    res=res+rem**l
    #print(res)
print(res)
if numb==res:
    print(numb,"is an armstrong number ")
else:
    print("Try again not an Armstrong number")