number = int(input('Write  a number to see the sum of odd number and prime numbers multiple by three:'))
sum = 0
count = 0
for n in range(0, number):
    if (n % 2) != 0 and (n % 3) == 0:
        sum = sum + n
        count = count + 1

print('The sum of {} it is {} with just {} prime numbers'.format(number, sum, count))

