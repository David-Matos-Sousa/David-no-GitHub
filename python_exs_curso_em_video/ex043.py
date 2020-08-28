print('Body Mass Index Calculator | kg/m² |')

height = float(input('What is your current height?'))
weight = float(input('What is your current weight?'))

bmi = weight / (height ** 2)

print('In base of your current height and weight you have {:.2f} of BMI'.format(bmi))

if bmi < 18.5:
    print('You are underweight')
elif bmi < 25:
    print('You are healthy')
elif bmi <= 30:
    print('You are obese')
elif bmi > 40:
    print('You are obese morbid')
