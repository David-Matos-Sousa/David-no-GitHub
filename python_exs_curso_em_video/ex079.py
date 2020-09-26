numbers = []

while True:
    new =(int(input('Please input some value:')))
    if new not in numbers:
         numbers.append(new)
         print('The number was add successfully')
    else:
         print('The number it is duplicated')
    c = str(input('Continue... YES or NO?'))
    if c == 'NO':
        break
print(f'Your list of values is {numbers}')

