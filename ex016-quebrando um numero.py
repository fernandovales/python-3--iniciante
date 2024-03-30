'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
import random
n = random.random()
print('a parte inteira de {} é {}'.format(n,trunc(n)))
