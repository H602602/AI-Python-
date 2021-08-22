def dectobin(n):
    if n==0:
        return 0
    else:
        dectobin(n//2)
    print(n%2)
dectobin(12)