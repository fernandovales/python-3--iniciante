'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''


peso = float(input('digite o peso da 1ª pessoa: '))
menor = peso
maior = peso
for cont in range (1,5):
    peso = float(input('digite o peso da {}ª pessoa: '.format(cont+1)))
    if peso >= maior :
        maior = peso
    if peso <= menor:
        menor = peso
print('o maior peso foi {}kg'.format(maior))
print('o menor peso foi {}kg'.format(menor))

