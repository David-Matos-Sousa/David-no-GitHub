from math import cos, sin, tan, radians
degrees = float(input('Write a grau number:'))
print('Did you wrote {}'.format(degrees))
print('The cosine of this number is {:.3f}'.format(cos(radians(degrees))))
print('The sine of this number is {:.3f}'.format(sin(radians(degrees))))
print('The tangent of this number is {:.3f}'.format(tan(radians(degrees))))
