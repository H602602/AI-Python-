a=int(input("Enter a number to know the sum of the digits"))
result=0
string=str(a)
for i in string:
    result=result+int(i)
print(result)