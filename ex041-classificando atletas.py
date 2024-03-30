'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

from datetime import date
atual = date.today().year
nasc = int(input('digite o ano do seu nascicmento: '))
idade = atual - nasc
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade <= 25:
    cat = 'SENIOR'
elif idade > 25;
    cat = 'MASTER'
print('Idade: {} anos'.format(idade))
print('Categoria: {}'.format(cat))
