'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('a hipotenusa é igual a {:.2f}'.format(h))
