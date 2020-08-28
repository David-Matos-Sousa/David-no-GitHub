first = int(input('Write a initial term of an arithmetic progression:'))
difference = int(input('Write a common difference:'))
term = first
cont = 1
while cont <= 10:
    print('{} -> '.format(term), end='')
    term += difference
    cont += 1
print('PAUSE')
print('Many terms {}'.format(cont-1))
aws_2 = int(input('How many terms did you wanna show more?'))
if  aws_2 == 0:
    print('Thank you!')
else:
    while aws_2 <= aws_2:
        print('{} -> '.format(term), end='')
        term += difference
        cont += 1
    print('PAUSE')