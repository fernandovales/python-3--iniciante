'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e
o menor valor digitado e as suas respectivas posições na lista.
'''

from random import randint
num = []
for c in range (0,5):
    num.append(randint(0,10))
maior = max(num)
menor = min(num)
print(f'os numeros foram {num}')
print(f'o maior valor foi {maior} nas posicoes ',end=' ')
for p, v in enumerate(num):
    if v == maior:
        print(f'{p}..',end=' ')
print()
print(f'o menor valor foi {menor} nas posicoes ',end=' ')
for p, v in enumerate(num):
    if v == menor:
        print(f'{p}...',end=' ')
print()
#for posicao, elemento in enumerate(num):
#    print(f'{posicao} ªposicao = {elemento}')



