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
