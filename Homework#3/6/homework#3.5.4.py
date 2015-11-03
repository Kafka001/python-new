def age_job(x):
    x = int(raw_input('Insert your age'))
    if 26 <= x <= 60:
        print 'you need to find a job'
    else:
        print 'errrrorrrr, this program is for human'
    return 'your age is %i'%x
print(age_job(1))