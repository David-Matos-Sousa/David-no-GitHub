from random import randint
# Generate a random number for the computer between 1 and 10
number_computer = randint(0, 10)

# Get a number of the player
number_player = 0

# Counter of tries
tries = 0

# Checking the value if the value is bigger or lower than the shot
while number_player != number_computer:

    number_player = int(input('Say a number between 1 and 10:'))
    tries += 1
    if number_player < number_computer:
        print('Number wrong! try again with a biggest number')
    elif number_player > number_computer:
        print('Number wrong! try again with a lower number')

print('Well done! You have taken {} tries to get it'.format(tries))
