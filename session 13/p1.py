a=int(input("Enter a number to know whether it is perfect or not"))
result=0
for i in range(1,a):
    if a%i==0:
        result=result+i
if result==a:
    print("Number is perfect")
else:print("Number is not perfect")