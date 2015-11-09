inp = int(input('insert figure from 0 to 9'))
class Qu:
    x = inp
    def __init__(self,x):
        if 0<=x<=3:
            def firstfunc(x):
                n = str(raw_input('insert data '))
                z = int(raw_input('how many times i need to show? '))
                return n*z
        elif 4<=x<=6:
            def secondfunc(x):
                for i in range(1,11):
                    print (x)
                    x += 1
        elif 7<= x <= 9:
            def thirdfunc(x):
                m = int(input('insert figure to count '))
                return x**m
        else:
            print('unavailable function')
b = Qu(inp)
print(b)

