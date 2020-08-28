gender = str(input('What is your gender [M/F]?')).strip().upper()[0]

while gender not in 'MF':
    gender = str(input('Wrong data please insert a correct option between M or F:')).strip().upper()[0]
print('Your gender {} was sucessful register'.format(gender))
