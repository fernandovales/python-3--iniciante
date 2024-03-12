
n = int(input('digite um numero para calcular seu fatorial: '))
fat = 1
for n in range(n,0,-1):
    fat *= n
    print('{}'.format(n),end='')
    print(' x 'if n > 1 else ' = ',end=' ' )
print('{}'.format(fat))

