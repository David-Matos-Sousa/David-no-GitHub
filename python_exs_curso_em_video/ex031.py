distance = float(input('What is the distance of your trip in KM?'))

if distance <= 200:
    print('The price of your trip you gonna cost {}'.format(distance * 0.50))
else:
    print('The price of your trip you gonna cost {}'.format(distance * 0.45))

