def age_young(x):
    x = int(raw_input('Insert your age'))
    if 0 <= x <= 7:
        print "you have to go to kindergarden"
    else:
        print 'errrrorrrr, this program is for human'
    return 'your age is %i'%x
print(age_young(1))