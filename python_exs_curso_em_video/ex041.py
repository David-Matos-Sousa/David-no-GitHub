from datetime import date

year = int(input('Write the birth year of the swimming athlete:'))

age = date.today().year - year

print('The age of athlete year is {}'.format(age))

if age <= 9:
    print('You are a little')
elif age <= 14:
    print('You are a infant')
elif age <= 19:
    print('You are a junior')
elif age <= 20:
    print('You are a senior')

else:
    print('You are a master')
