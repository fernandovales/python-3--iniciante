

from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('a hipotenusa é igual a {:.2f}'.format(h))
