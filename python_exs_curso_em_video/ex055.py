weights = []
for person in range(1, 6):
    weight = float(input('What is the weight of {}ª person:'.format(person)))
    weights += [weight]

print('The biggest weight it is {}'.format(max(weights)))
print('The smallest weight it is {}'.format(min(weights)))
