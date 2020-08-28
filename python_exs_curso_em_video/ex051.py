term = int(input('Write a initial term of an arithmetic progression:'))
difference = int(input('Write a common difference:'))
tenth = term + (10 - 1) * difference
for n in range(term, tenth + difference, difference):
    print(n)