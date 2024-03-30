'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

saque = int(input('digite o valor do saque:'))
restosaque = saque
while restosaque !=0:
    ced50 = saque // 50
    restosaque = saque - ced50*50
    ced20 = restosaque // 20
    restosaque = restosaque-ced20*20
    ced10 = restosaque // 10
    restosaque = restosaque-ced10*10
    ced1 = restosaque // 1
    restosaque = restosaque-ced1*1
print(f'cedula 50:{ced50} cedula 20:{ced20} cedula 10:{ced10} cedula1:{ced1}')
if ced50 > 0:
    print(f'{ced50} notas de 50 R$.')
if ced20 > 0:
    print(f'{ced20} notas de 20 R$.')
if ced10 > 0:
    print(f'{ced10} notas de 10 R$')
if ced1 > 0:
    print (f'{ced1} notas de 1 R$')
print('SAQUE REALIZADO COM SUCESSO.')

