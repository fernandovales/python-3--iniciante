'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.
'''

p1 = int(input('digite o premeiro termo da PA: '))
razao = int(input('digite a razao da PA: '))
cont = 1
while cont <= 10:
    print('{}'.format(p1),end='-')
    p1 += razao
    cont += 1
print('FIM')
