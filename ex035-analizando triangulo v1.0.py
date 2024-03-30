'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo
'''

r1 = float(input('digite o comprimento de r1: '))
r2 = float(input('digite o comprimento de r2: '))
r3 = float(input('digite o comprimento de r3: '))
if r1+r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
     print('pode sim formar um triangulo! ')
else:
    print('não pode formar um triangulo!')
