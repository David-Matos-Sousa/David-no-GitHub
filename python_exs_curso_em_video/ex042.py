first_length = float(input('Say the first length:'))
second_length = float(input('Say the second length:'))
third_length = float(input('Say the third length:'))

if first_length < (second_length + third_length) and second_length < third_length + first_length and third_length < first_length + second_length:
    print('With this number can be a triangle and...\n')
    if first_length == second_length == third_length:
        print('This is a equilateral triangle')
    elif first_length != second_length != third_length:
        print('This is a scalene triangle')
    elif first_length == second_length != third_length or third_length == second_length != first_length or first_length == third_length != second_length:
        print('This is a isosceles triangle')

else:
    print('This is not a triangle')
