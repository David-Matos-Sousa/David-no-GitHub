user = 0
even = 0
for n in range(0, 6):
    n = int(input('Write a number integrate:'))
    if n % 2 == 0:
        user = n + user
        even += 1
print('Did you inform {} even numbers and the sum of this numbers is {}'.format(even,user))
