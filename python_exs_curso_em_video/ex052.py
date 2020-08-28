num = int(input('Write a number:'))
div = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        div = div + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m The number {} was divisible {} times'.format(num, div))
if div == 2:
    print('It is a prime')
else:
    print('It is not a prime')
