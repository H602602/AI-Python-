a=int(input("Enter your english marks"))
b=int(input("Enter your maths marks"))
c=int(input("Enter your sst marks"))
d=int(input("Enter your science marks"))

e=a+b+c+d
print(e)
f=e/500
print(f)
g=f*100
print(g)

if g>90:
    print("Excellent")
elif g>80:
    print("A")
elif g>70:
    print("B")
elif g>60:
    print("C")
elif g>50:
    print("D")
elif g<50:
    print("F")
