'''
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

from faker import Faker
from random import randint
fake = Faker()                                  #inicializar a biblioteca
temp = []                                       #lista temporaria
princ = []                                      #listaprincipal
mai = men = 0                                   #variaveis para guardar maior e menor peso
pesos= []                                       #lista com todos os pesos
while True:
    temp.append(fake.first_name_female())
    temp.append(randint(45,200))
    princ.append(temp[:])                           #cópia da lista temporaria
    pesos.append(temp[1])                           #add todos os pesos numa lista só
    temp.clear()                                    #limpando lista temorária para não haver duplicidade
    resp = str(input('quer continuar? [S/N]: '))
    if resp in 'Nn':                                #condição de parada
        break
mai = max(pesos)                                    #pegando o maior e o menor peso da lista de todos os pesos
men = min(pesos)
print(f'voce cadastrou {len(princ)} pessoas. ')     #tamnaho da lista completa
print(f'maior peso foi {mai} kg. Peso de ',end='')
for p in princ :                                    #varrer toda a lista principal
    if p [1] == mai:                                #quando o peso do elemento for igual ao maior peso
        print(f'[{p[0]}]',end='')                   #mostre o nome
print()
print(f'menor peso foi {men} kg. peso de ',end='')
for p in princ :
    if p[1] == men :
        print(f'[{p[0]}]',end='')
print()
