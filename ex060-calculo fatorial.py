num = int(input('digite um numero: '))
fat = 1
cont = num
while cont > 0:
    fat = cont * fat
    print('{}x'.format(cont),end='')
    cont -= 1
print(' = {}'.format(fat))



