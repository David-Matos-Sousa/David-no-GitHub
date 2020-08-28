grade1 = float(input('What is your first grade:'))
grade2 = float(input('What is your second grade:'))

mean = (grade1 + grade2)/2

print('Hi the mean of semester is {}'.format(mean))

if mean < 5:
    print('With this grades you are disapproved on the semester :(')
elif 5 <= mean < 7:
    print('With this grades you are in school recovery o/')
elif mean >= 7:
    print('Congrats you are approved on college =)')
