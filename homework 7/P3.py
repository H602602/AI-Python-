def naturalnumber(n):
    if n<=1:
        return n
    else:
        return n + naturalnumber(n-1)
num=6
print(naturalnumber(num))
