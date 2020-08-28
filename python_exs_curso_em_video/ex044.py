shopping = float(input('What is the price of your shopping?'))

print('[1] pay for in cash')
print('[2] pay for in credit card one lump sum on')
print('[3] pay for in credit card two installments')
print('[4] pay for in credit card three or more installments')

condition = int(input('What form did you pretend to pay?'))

if condition == 1:
    print('You will have to pay {}'.format(shopping*0.9))
elif condition == 2:
    print('You will have to pay {}'.format(shopping*0.95))
elif condition == 3:
    print('You will have to pay {}'.format(shopping))
else:
    print('You will have to pay {}'.format(shopping*1.20))
