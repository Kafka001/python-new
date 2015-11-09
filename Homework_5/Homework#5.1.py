y = int(input('insert figure from 0 to 9 '))
class Qu:
    def __init__(self,y):
        if 0 <= y <= 3:
            n = str(raw_input('insert data '))
            z = int(raw_input('how many times i need to show? '))
            print (n*z)
        elif 4 <= y <= 6:
            for i in range(1,11):
                print (y)
                y += 1
        elif 7 <= self.x <= 9:
            m = int(input('insert figure to count '))
            print y**m
        else:
            print('unavailable function')
b = Qu(y)
print(b)