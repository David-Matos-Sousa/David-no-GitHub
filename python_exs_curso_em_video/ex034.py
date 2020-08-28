salary = float(input('What is your salary per month?'))

if salary > 1250:
    print('You have received a salary increase of 10%, so you current salary is gonna be {}'.format(salary * 1.1))
if salary <= 1250:
    print('You have received a salary increase of 15%, so you current salary is gonna be {}'.format(salary * 1.15))
