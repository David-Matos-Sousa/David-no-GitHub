maior = 0
menor = 0
for balanca in range(1, 4):
    print('========{}========='.format(balanca))
    peso = float(input('Qual seu peso?'))
    if balanca == 1:
        maior = peso
        menor = peso
    elif peso > maior:
            maior = peso
    elif peso < menor:
            menor = peso
print('O que pesa mais possui {} kg'.format(maior))
print('O que pesa menos possui {} kg'.format(menor))
