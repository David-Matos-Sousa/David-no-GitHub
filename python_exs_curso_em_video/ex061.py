first = int(input('Write a initial term of an arithmetic progression:'))
difference = int(input('Write a common difference:'))
term = first
cont = 1
while cont <= 10:
    print('{} -> '.format(term), end='')
    term += difference
    cont += 1

print('Many terms {}'.format(cont-1))
