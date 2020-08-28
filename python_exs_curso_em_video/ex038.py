number1 = int(input('Write one integrate number:'))
number2 = int(input('Write other integrate number:'))
print('In comparison...')

if number1 > number2:
    print('First number {} is the biggest'.format(number1))
elif number2 > number1:
    print('Second number {} is the biggest'.format(number2))
elif number2 == number1:
    print('The two number are equals')
else:
    print('Please answer with a integrate number :) ')
