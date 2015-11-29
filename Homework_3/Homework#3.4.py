def newfunc(*args):
    x = 1
    rec = [x**i for i in args]
    return rec
print newfunc(1,2,3)# still don't work... don't know why...
