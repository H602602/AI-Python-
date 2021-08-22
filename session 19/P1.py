def Dectobinary(n):
    if n>=1:
        Dectobinary(n//2)
    print(n%2,end=" ")
n=20
Dectobinary(n)
    
    
        

