inp = int(raw_input('insert integer from 0 to 9 '))
def firstfunc():
    n = str(raw_input('insert data '))
    z = int(raw_input('how many times i need to show? '))
    return n*z
def secondfunc():
    rrr = inp
    for i in range(1,11):
        print (rrr)
        rrr += 1
def thirdfunc():
    jujuju = inp
    m = int(input('insert figure to count '))
    return jujuju**m

if 0<=inp<=3:
    print(firstfunc())
elif 4<=inp<=6:
    print(secondfunc())
elif 7<=inp<=9:
    print(thirdfunc())
else:
    print('unavailable function')


