def newfunc (x):
    x = str(raw_input('Insert summary of your investigation: '))
    t = [(len(y),y) for y in x.split(' ')]
    t = dict(t)
    if x != 0:
        print (t)
    else:
        print ('there is no data. good day')
print(newfunc(1))