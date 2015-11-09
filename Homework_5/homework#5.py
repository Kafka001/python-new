inp = int(input('insert figure from 0 to 9'))
class Qu:
    def __init__(self,x):
        if 0 <= x <= 3:
            def firstfunc(self):
                n = str(raw_input('insert data '))
                z = int(raw_input('how many times i need to show? '))
                return n*z
            print(firstfunc(self))
        elif 4 <= x <= 6:
            def secondfunc(self):
                x = inp
                for i in range(1,11):
                    print (x)
                    x += 1
            print(secondfunc(self))
        elif 7 <= x <= 9:
            def thirdfunc(inp):
                m = int(input('insert figure to count '))
                return x**m
            print(thirdfunc(self))
        else:
            print('unavailable function')
b = Qu(inp)
print(b)

