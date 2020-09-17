p = float(input("Principal : "))
r = float(input("Rate (%) : "))
t = int(input("Time : "))
n = int(input("Number of times the interest is compounded per year : "))
ci = p*(1+(r/n))**(n*t) 
si = (p*r*t)/100

print("Compound Interest :",ci)
print("Simple Interest :",si)