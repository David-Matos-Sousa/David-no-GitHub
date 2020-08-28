ageman = 0
namemans = ''
f = 0
ages = 0

for person in range(1, 5):
    print('|{}|'.format(person))

    name = str(input('Name:')).strip()

    age = int(input('Age:'))

    gender = str(input('Gender [M|F]:')).strip().upper()

    ages += age

    mean_ages = ages / 4

    if person == 1 and gender == 'M':
        namemans = name
        ageman = age
    if gender == 'M' and age > ageman:
        ageman = age
        namemans = name

    if age < 20 and gender == 'F':
        f += 1

print('The oldest man in the group is {} with {} year old'.format(namemans, ageman))
print('The mean ages of group is {}'.format(mean_ages))
print('This group had {} women less than 20 years old'.format(f))
