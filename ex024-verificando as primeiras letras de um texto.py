'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

nome = str(input('Qual é o nome da sua cidade? ')).strip()
print('Essa cidade começa com "Santo"? ')
print(nome[0:6].lower() == 'santo ')
