x = int(input('insert integer from 0 to 9'))
if 0<= x <= 3:
    n = str(raw_input('insert data '))
    z = int(raw_input('how many times i need to show? '))
    print (n*z)
elif 4 <= x <= 6:
    for i in range(1,11):
        print (x)
        x += 1
elif 7<= x <=9:
    m = int(input('insert figure to count '))
    print x**m
else:
    print('unavailable function')
