from math import trunc

number = float(input('Write a number with decimals to know the integrate part:'))

integrate = trunc(number)

print('So the integrate part of {} this number is {}'.format(number, integrate))
