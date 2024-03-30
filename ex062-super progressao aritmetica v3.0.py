'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.
'''

p1 = int(input('primeiro termo da PA:'))
razao = int(input('razão da PA:'))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total +=  mais
    while cont <= total:
        print('{}'.format(termo),end=' ')
        print('-' if cont < total else ' ',end='')
        termo += razao
        cont += 1
    print('PAUSA...')
    mais = int(input('quantos termos a mais? '))
print('PA finalizada com {} termos'.format(total))




