city = str(input('Write the name of the city that you were born:')).strip()
print('Your city is {}'.format(city))
print('Tem SANTO no nome? {}'.format(city[:5].upper() == 'SANTO'))
