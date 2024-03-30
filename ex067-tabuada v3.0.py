'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    n = int(input('quer ver a tabuada de que numero? '))
    if n < 0:
        break
    for cont in range(0, 11):
        print(f'{n} x {cont} = {n * cont}')
    print('-'*20)
print('FIM')
