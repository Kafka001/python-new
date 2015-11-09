from Homework_4 import *

inp = int(raw_input('insert integer from 0 to 9 '))
if 0<=inp<=3:
    print(firstfunc())
elif 4<=inp<=6:
    print(secondfunc())
elif 7<=inp<=9:
    print(thirdfunc())
else:
    print('unavailable function')