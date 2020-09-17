
num = ( int(input('Fist number:')), int(input('Second number:')), int(input('Third number:')), int(input('Last number:')))

print('You put this numbers:',num)

if 9 in num:
    print('The number 9 appears {} times'.format(num.count(9)))
else: 
    print("Don't have the number 9")

if 3 in num:
    print('The number 3 appears in {} position'.format(num.index(3)+1))
else: 
    print("Don't have the number 3")

print('The even numbers are:')
for n in num:
    if n % 2 == 0:
        print(n)
    