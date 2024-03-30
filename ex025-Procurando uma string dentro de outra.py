'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = str(input('digite o nome completo: ')).strip()
print('silva' in nome.lower())
