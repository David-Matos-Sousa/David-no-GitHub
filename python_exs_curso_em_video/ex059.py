# Get the values
first_one = float(input('Write a first number:'))
second_one = float(input('Write a second number:'))

# Get the move
move = 0

# Showing the moves

while move != 5:
    print('''    [1] SUM
    [2] MULTIPLY
    [3] BIGGER
    [4] NEW NUMBERS
    [5] EXIT APPLICATION ''')
    move = int(input('What is your move?'))
    if move == 1:
        print('The sum between {} and {} is {}'.format(first_one, second_one, (first_one + second_one)))
    elif move == 2:
        print('The multiplication between {} and {} is {}'.format(first_one, second_one, (first_one * second_one)))
    elif move == 3:
        if first_one > second_one:
            print('The biggest number between {} and {} is {}'.format(first_one, second_one, first_one))
        else:
            print('The biggest number between {} and {} is {}'.format(first_one, second_one, second_one))
    elif move == 4:
        print('Write new numbers...')
        first_one = float(input('Write a first number:'))
        second_one = float(input('Write a second number:'))

print('Thank you for using the application =)')



