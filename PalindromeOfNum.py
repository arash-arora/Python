num = int(input("Number (num>1000): "))
rem=0
rev=0
while(num!=0):
    rem=num%10
    num=num//10
    rev = rem +rev*10
print(rev)