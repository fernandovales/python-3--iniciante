p1 = int(input('digite o premeiro termo da PA: '))
razao = int(input('digite a razao da PA: '))
cont = 1
while cont <= 10:
    print('{}'.format(p1),end='-')
    p1 += razao
    cont += 1
print('FIM')
