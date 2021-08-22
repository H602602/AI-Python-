a=int(input("Enter your electricity bill(in units)"))
if a<100:
    b=0
elif a<200:
    a=(a-100)
    b=a*5
elif a>200:
    b=(a-200)*10+500
print(b)