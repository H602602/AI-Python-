a=int(input("Enter your marks"))
b=int(input("Enter your marks"))
c=int(input("Enter your marks"))
average=a+b+c/3
if a<33 or b<33 or c<33:
    print("You have failed your test")
elif average<40:
    print("You have failed the test")
else:
    print("You have passed your test")
