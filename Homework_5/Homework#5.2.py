x = int(raw_input("Please insert your age"))
class ZuZu:
    y = x
    def kinderg(self):
        return "you have to go to kindergarden"
    def school(self):
        return "you have to go to school"
    def collage(self):
        return "you need to go to collage"
    def job(self):
        return 'you need to find a job'
    def oldman(self):
        return 'you can do whatever you want! you deserved it!'
    def __init__(self,y):
        if 0 <= y <= 7:
            print(y.kinderg())
        elif 8 <= y <= 18:
            print(y.school())
        elif 19 <= y <= 25:
            print(y.collage())
        elif 26 <= y <= 60:
            print(y.job())
        elif 61 <= y <= 120:
            print(y.oldman())
        else:
            print ('errrrorrrr, this program is for human')
b = ZuZu(x)
print(b)