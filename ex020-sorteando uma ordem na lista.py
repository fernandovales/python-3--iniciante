'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
n1 = str(input('nome 1: '))
n2 = str(input('nome 2: '))
n3 = str(input('nome 3: '))
n4 = str(input('nome 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem será : ')
print(lista)
