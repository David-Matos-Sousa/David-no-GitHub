#from math import pow
from math import hypot
opposite = float(input('Write the number of the opposite side of right angle:'))
longest = float(input('Write the number of the longest side of right angle:'))

#hypotenuse = pow((pow(opposite, 2) + pow(longest, 2)), 1/2)

print('The hypotenuse is {:.3f}'.format(hypot(opposite, longest)))

