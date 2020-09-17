names = ('David','Karina','Veryjhonssons','Andrade')

for name in names:
    print(f'\n In the name {name.upper()} we have ', end='')
    for letter in name:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

