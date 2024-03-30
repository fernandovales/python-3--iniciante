'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

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

