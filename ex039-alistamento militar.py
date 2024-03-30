'''
 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
 tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
ano = int(input('Em que ano voce nasceu:'))
idade = date.today().year - ano
gen = str(input('Informe seu sexo [M] ou [F]:'))
if gen.lower() == 'f':
    print('Voce tem {} anos em {}'.format(idade,date.today().year))
    print('Seu allistamento não e obrigatorio')
elif idade < 18 and gen.lower() =='m':
    print('Você terá que se alistar.')
    print('Saltam  {} anos para seu alistamento'.format(18-idade))
    print('Seu alistamento sera nem {}'.format(date.today().year +(18-idade)))
elif idade == 18 and gen.lower() =='m':
    print('É hora de se alistar')
else:
    print('Já passou o tempo do alistamento.')
    print('Passaram {} anos '.format(idade-18))
    print('Seu alistamento foi em {}'.format(date.today().year -(idade -18)))




