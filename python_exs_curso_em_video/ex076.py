compras =('Pao', 4, 'Cafe', 6, 'Leite', 8, 'Arroz', 60)

for pos in range(0, len(compras)):
    if pos % 2 ==0:
        print(f'{compras[pos]:<}', end='')
    else:
        print(f' R$ {compras[pos]:>}')