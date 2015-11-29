class Juk:
    inp = int(raw_input('insert integer from 0 to 9 '))
    def __init__(self):
        pass

class KuKu(Juk):
    def firstfunc(self):
        n = str(raw_input('insert data '))
        z = int(raw_input('how many times i need to show? '))
        return n*z
    def secondfunc(self):
        for i in range(1,11):
            print (self.inp)
            self.inp += 1
    def thirdfunc(self):
        jujuju = self.inp
        m = int(input('insert figure to count '))
        return jujuju**m

class ZuZu(Juk,KuKu):
    def __init__(self):
        super(ZuZu, self).__init__(self)
        if 0<= self.inp <=3:
            print(self.firstfunc())
        elif 4<=self.inp<=6:
            print(self.secondfunc())
        elif 7<=self.inp<=9:
            print(self.thirdfunc())
        else:
            print('unavailable function')

n = ZuZu()
print(n)