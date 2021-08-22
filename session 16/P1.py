def twostring(a,b):
    firstlet=a[0]+b[0]
    middlelet=a[int(len(a) / 2):int(len(a) / 2) + 1] + b[int(len(b) / 2):int(len(b) / 2) + 1]
    lastlet=a[-1]+b[-1]
    final=firstlet+middlelet+lastlet
    print(final)
twostring("america","japan")

