a=int(input("Enter a number to know whether it is prime or not"))
prime=True

for i in range(2,a):
    if a%i==0:
        prime=False
    else:continue
if prime==True:
    print(a ,"is a prime number")
else:print(a,"is prime number")