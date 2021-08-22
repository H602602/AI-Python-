def factorial(num):
    p=1
    for i in range(1,num+1):
        p=p*i
    return p
a=int(input("Enter a number"))
print("factorial of",a,"is",factorial(a))