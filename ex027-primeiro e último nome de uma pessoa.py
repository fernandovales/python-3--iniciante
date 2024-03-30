'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''


nome = str(input('digite o nome completo: ')).strip()
div = nome.split()
print(div)
print('primeiro nome:{}'.format(div[0]))
print('ultimo nome: {}'.format(div[nome.count(' ')]))
