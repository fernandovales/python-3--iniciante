'''
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

from faker import Faker
from random import randint
fake = Faker()
temp = []
princ = []
mai = men = 0
while True:
    temp.append(fake.first_name_female())
    temp.append(randint(45,200))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'voce cadastrou {len(princ)} pessoas. ')
print(f'maior peso foi {mai} kg. Peso de ',end='')
for p in princ :
    if p [1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'{princ}')
print(f'menor peso foi {men} kg. peso de ',end='')
for p in princ :
    if p[1] == men :
        print(f'[{p[0]}]',end='')
print()





