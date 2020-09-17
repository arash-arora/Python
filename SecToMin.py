sec=float(input("Enter the seconds : "))
rem=0
if sec%60==0:
    minutes=sec/60
else:
    rem=sec%60
    minutes = sec//60
print(minutes,"minutes",rem,"seconds")