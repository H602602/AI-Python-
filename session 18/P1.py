def diagonaldiff(a,b):
    d1=0
    d2=0
    for i in range(0,b) :
        for j in range(0,b):
            if i == j :
                d1 +=a[i][j]
            if i==b-j-1:
                d2+=a[i][j]
    print(d1-d2)
a=3
b=[[11, 2, 4],
[4 , 5, 6],
[10, 8, -12]]
diagonaldiff(a,b) 



