speed = float(input('What is the speed of the car?'))

print('You was driven with this {:.1f}'.format(speed))

if speed > 80:
    print('You received a traffic ticket by exceed the speed limit ')
    print('You have to pay {:.1f} in total for each Km exceed'.format((speed-80)*7))
else:
    print('Nice you were follow the rules :)')