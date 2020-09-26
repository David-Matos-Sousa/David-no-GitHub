# add um item no final da lista = append(item)
# add um item numa posição da lista = inset(0,item)
# deletar um item da lista = del lista[posição]
# deletar um item da lista = lista.pop[posição]
# deletar um item da lista = lista.remove(item)
# colocar lista em orderm = lista.sort()

list = []

for values in range(0,6):
    list.append(int(input('Please input some value:')))

list.sort

print('The bigger number is',max(list))
print('The smaller number is',min(list))