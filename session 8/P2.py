a=int(input("How you want to enter the temperarure 1-celcius 2-ferenheit"))
b=int(input("Enter the temperarure"))
if a==1:
    print(b*9/5+32)
elif a==2:
    print(b-32*5/9)
else:print("Invalid please enter 1 or 2")
