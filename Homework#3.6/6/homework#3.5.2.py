def age_school(x):
    x = int(raw_input('Insert your age'))
    if 8 <= x <= 18:
        print 'you have to go to school'
    else:
        print 'errrrorrrr, this program is for human'
    return 'your age is %i'%x
print(age_school(1))