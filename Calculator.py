a = int(input("Operand 1 : "))
b = int(input("Operand 2 : "))
op = input("Operator : ")
if op=='+':
    print("Sum :",a+b)
elif op=='-':
    print("Difference :",a-b)
elif op=='/':
    print("Division :",a/b)
elif op=='*':
    print("Multiplication :",a*b)
else:
    print("Invalid")