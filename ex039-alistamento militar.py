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




