number = str(input('Write a number enter 0 and 9999:'))
print('This number {}'.format(number))
print('Have {} units'.format(number[3]))
print('Have {} decimals'.format(number[2]))
print('Have {} hundreds'.format(number[1]))
print('Have {} thousands'.format(number[0]))

number2 = int(input('Write a number enter 0 and 9999:'))

print('This number {}'.format(number2))
print('Have {} units'.format(number2 // 1 % 10))
print('Have {} decimals'.format(number2 // 10 % 10))
print('Have {} hundreds'.format(number2 // 100 % 10))
print('Have {} thousands'.format(number2 // 1000 % 10))
