from datetime import date

age = int(input('What is your year of birth?'))

enlistment = date.today().year - age

if enlistment == 18:

    print('You have to do the military enlistment now! Case you have {} years'.format(enlistment))

elif enlistment < 18:

    print('You steel need to do the military enlistment! Case you have only {} years'.format(enlistment))

elif enlistment > 18:

    print('You already late for the military enlistment, case you have {} years '.format(enlistment))

