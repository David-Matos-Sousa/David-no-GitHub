number = float(input('Write how much money have on your bank account right now:'))
dollar = float(input('What is the dollar quote today?'))

print('So with this money ${:.2f}, you can buy ${:.2f} dollars'.format(number, (number/dollar)))

