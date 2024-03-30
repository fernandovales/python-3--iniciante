'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1,6)

print('=-'*20)
print('  SORTEANDO VALORES  ')
print('=-'*20)

for k, v in jogo.items():
    print(f'O {k} tirou : {v}')
    sleep(1)

ranking = list()
ranking = sorted(jogo.items(),key = itemgetter(1),reverse= True)

print('=-'*20)
print('   RANKING DOS JOGADORES ')
print('=-'*20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)



