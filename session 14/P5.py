def factorial(x):
    if x==0 or x==1:
        return 1
    else :
        return x*factorial(x-1)
a=int(input("Enter a number"))
print(f"the factorial of {a} is {factorial(a)}")
# n=5
# factorial(5)=5*factorial(4)=5*24=120
# factorial(4)=4*factorial(3)=4*6=24
# factorial(3)=3*factorial(2)=3*2=6
# factorial(2)=2*factorial(1)=2*1=2
# factorial(1)=1