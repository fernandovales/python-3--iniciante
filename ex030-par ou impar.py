'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''


n = int(input('digite um numero inteiro: '))
if n % 2 == 0:
    print('{} é um numero PAR'.format(n))
else:
    print('{} é um numero IMPAR'.format(n))

print('PAR' if n%2 == 0 else 'IMPAR') #SIMPLIFICANDO
