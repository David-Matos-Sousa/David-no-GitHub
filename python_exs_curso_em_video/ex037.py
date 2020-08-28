number = int(input('Write a number integrate:'))
option = int(input('Choose 1 for converter to binary\nChoose 2 for converter to octal\nChoose 3 for converter to '
                   'hexadecimal\nAnswer:'))
if option == 1:
    print('Your number in binary is {}'.format(bin(number)[2:]))
elif option == 2:
    print('Your number in octal is {}'.format(oct(number)[2:]))
elif option == 3:
    print('Your number in hexadecimal is {}'.format(hex(number)[2:]))
else:
    print('Choose the number correctly!')

