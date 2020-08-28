housevalue = float(input('What is the house value today?'))
salaryvalue = float(input('What is the salary value today?'))
years = float(input('How many year did you pretend to pay the house?'))

installments = housevalue/(years*12)

if installments >= (salaryvalue*0.03):
    print('Bank loan denied')
else:
    print('Congrats you will pay in {} years, about {:.2f}$ per month for paying the house that costs {}$'.format(years, installments, housevalue))
