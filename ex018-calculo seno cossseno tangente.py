'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians,sin , cos , tan
an = float(input('informe um angulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('o seno é {:.2f} \n o cosseno é {:.2f} \n e a tangente é {:.2f}'.format(sen,cos,tan))
