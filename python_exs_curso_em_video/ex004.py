algo = input('Digite algo:')

print('Voce digitou {}, ele é da classe {}. Possui as seguintes propriedades:'.format(algo, type(algo)))

print('é numerico:{}'.format(algo.isnumeric()))

print('é alfanumerico:{}'.format(algo.isalnum()))
print('é texto:{}'.format(algo.isalpha()))
print('é decimal:{}'.format(algo.isdecimal()))
print('é alguma coisa que nao sei:{}'.format(algo.isascii()))
print('é um digito:{}'.format(algo.isdigit()))
print('é um indentificador:{}'.format(algo.isidentifier()))
print('esta em minuscula',algo.islower())