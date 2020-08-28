number_1 = float(input('Write the first number:'))
number_2 = float(input('Write the second number:'))
number_3 = float(input('Write the third number:'))

if number_1 > number_2 and number_1 > number_3:
    print('The biggest number this {}'.format(number_1))

if number_2 > number_1 and number_2 > number_3:
    print('The biggest number is {}'.format(number_2))

if number_3 > number_2 and number_3 > number_1:
    print('The biggest number is {}'.format(number_3))

if number_1 < number_2 and number_1 < number_3:
    print('The lowest number this {}'.format(number_1))

if number_2 < number_1 and number_2 < number_3:
    print('The lowest number is {}'.format(number_2))

if number_3 < number_2 and number_3 < number_1:
    print('The lowest number is {}'.format(number_3))