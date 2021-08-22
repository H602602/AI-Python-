def greatestnum(a,b,c):
    if a>b and a>c:
        greatest=a
    elif a<b and b>c:
        greatest=b
    else:
        greatest=c
    print(f"greatest number of {a},{b} and {c} is {greatest}")
greatestnum(1000,9888,870)
 