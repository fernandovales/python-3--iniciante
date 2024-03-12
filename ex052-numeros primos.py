num = int(input('digite um numero inteiro: '))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[1;32m{}\033[m'.format(c),end = ' ')
        cont = cont + 1
    else:
        print('{}'.format(c), end = ' ')
print('\n o numero {} tem {} divisores portanto:'.format(num, cont))
if cont == 2:
    print('É PRIMO.')
else :
    print('NÃO É PRIMO.')


