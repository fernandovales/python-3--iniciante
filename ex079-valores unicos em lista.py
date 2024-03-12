num = list()
while True:
    valor = int(input('digite um numero: '))
    if valor in num:
        print('valor duplicado.nao add a lista')
    else:
        num.append(valor)
        print('add com sucesso!')
    res =' '
    while res not in 'SN':
        res = str(input('quer continuar? [S/N]')).strip().upper()
    if res == 'N':
        break
num.sort()
print(f'voce digitou os numeros {num}')

