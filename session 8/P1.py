print("Hello I am a mini calculator")
print("I can do addition subtraction multiplication etc")
a=int(input("enter 1-addition 2-subtraction 3-multiplication 4-division 5-power 6-odd and even: "))
if a==1:
    b=int(input("Enter a number you want to add"))
    c=int(input("Enter second number you want to add with first"))
    print(b+c)

elif a==2:
    d=int(input("Enter a number you want to subtract"))
    e=int(input("Enter second number you want to subtract with first"))
    print(d-e)

elif a==3:
    f=int(input("Enter a number you want to multiply"))
    g=int(input("Enter second number you want to multiply with first"))
    print(f*g)

elif a==4:
    h=int(input("Enter a number you want to divide"))
    i=int(input("Enter second number you want to divide with first"))
    print(h/i)

elif a==5:
    j=int(input("Enter a number you want to count power"))
    k=int(input("Enter the power you want to count of"))
    print(pow(j,k))
elif a==6:
    l=int(input("Enter a number you want to know whether its odd or even "))
    if l%2==0:
        print("You number is even")
    else:print("Youe number is odd")
    
else:print("Invalid please enter 1,2,3,4,5 or 6")


