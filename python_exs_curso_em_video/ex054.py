from datetime import date

major = 0
younger = 0

for x in range(1, 8):
    x = int(input('What year the {}ª person was born?'.format(x)))
    if date.today().year - x >= 21:
        major = major + 1
    elif date.today().year - x <= 21:
        younger = younger + 1
    else:
        print('WTF')
print('You had {} people in majority and {} in minority!'.format(major, younger))
