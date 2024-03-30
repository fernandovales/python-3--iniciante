'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import  choice
nome1 = input('primeiro nome: ')
nome2 = input('segundo nome: ')
nome3 = input('terceiro nome: ')
nome4 = input('quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
s = choice(lista)
print('o escolhido em 2024 foi {}'.format(s))
