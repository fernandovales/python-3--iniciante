'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

num = int(input('digite um numero: '))
fat = 1
cont = num
while cont > 0:
    fat = cont * fat
    print('{}x'.format(cont),end='')
    cont -= 1
print(' = {}'.format(fat))



