'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint                              #Importa as funções randint do módulo random e sleep do módulo time.
from time import sleep
palpites = list()
jogos = list()
quant = int(input('quantos jogos voce quer? '))
tot = 1
while tot <= quant:                                     #Inicia um loop que será executado até que a variável tot seja maior que a quantidade desejada (quant).
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    tot += 1
print('-='*5,f'SORTEANDO {quant} JOGOS','-='*5)
for i,p in enumerate(jogos) :
    print(f'jogo {i+1} : {p}')
    sleep(1)
print('-='*5,'< BOA SORTE! >','-='*5)


