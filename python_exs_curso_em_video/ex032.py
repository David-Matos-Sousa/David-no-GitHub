from datetime import date

year = int(input('Say any year to know if is a leap:'))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Is a Leap Year \o/')

else:
    print('Is not a Leap Year :)')



