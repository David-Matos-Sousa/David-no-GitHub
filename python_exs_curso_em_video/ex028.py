from random import randint

number_int = randint(1, 5)

user_tentative = int(input('Write a number between 1 and 5 to guess what number the computer have decided:'))

if user_tentative == number_int:
    print('Congrats you win! The number is {}'.format(number_int))
else:
    print('Sorry try again the number is {}'.format(number_int))

print('GAME OVER')
