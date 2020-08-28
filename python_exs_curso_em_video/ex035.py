first_length = float(input('Say the first length:'))
second_length = float(input('Say the second length:'))
third_length = float(input('Say the third length:'))

if first_length < (second_length + third_length) and second_length < third_length + first_length and third_length < first_length + second_length:
    print('With this number can be a triangle')

else:
    print('This is not a triangle')

