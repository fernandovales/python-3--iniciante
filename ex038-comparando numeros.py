'''
 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
'''

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
if n1 > n2:
    print('O primeiro é maior.')
elif n2 > n1:
    print('O segundo é maior.')
else:
    print('Os numeros são iguais.')

