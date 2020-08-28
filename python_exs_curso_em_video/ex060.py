number = int(input('Write a number:'))
mulplicador = number
total = 1
while mulplicador > 0:
    print('{}'.format(mulplicador))

    total = mulplicador * total
    mulplicador -= 1
print(total)
