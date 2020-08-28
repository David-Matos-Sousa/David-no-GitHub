days = int(input('How many days did you rent the car?'))
km = float(input('How many Km did you drive?'))
price = (days * 60) + (km * 0.15)
print('Thanks for using our services :) You have to pay ${}'.format(price))
