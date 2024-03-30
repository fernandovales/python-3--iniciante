'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteio (lista):
    for c in range(5):
        lista.append(randint(0,10))
    print(f'os numeros sorteados foram {lista}')

def soma(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'a soma dos pares em  {lista}  foi  {s} ')
num = []
sorteio(num)
soma(num)




