def age_collage(x):
    x = int(raw_input('Insert your age'))
    if 19 <= x <= 25:
        print 'you have to go to collage'
    else:
        print 'errrrorrrr, this program is for human'
    return 'your age is %i'%x
print(age_collage(1))