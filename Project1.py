#-*- coding:utf-8 -*-
import math
x = int(raw_input(u"Пожалуйста введите свой возраст  " ))
if 0 <= x <= 7:
    print ("you have to go to kindergarden")
elif 8 <= x <= 18:
    print ("you have to go to school")
elif 19 <= x <= 25:
    print ("you need to go to collage")
elif 26 <= x <= 59:
    print ('you need to find a job')
elif 60 <= x <= 120:
    print('you can do whatever you want! you deserved it!')
else:
    print ('errrrorrrr, this program is for human')