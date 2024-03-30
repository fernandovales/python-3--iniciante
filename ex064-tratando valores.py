'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
eles (desconsiderando o flag).
'''

soma = num = totn = 0
while num != 999:
    num = int(input('digite um numero: '))
    if num != 999:
        soma = soma + num
        totn += 1
    else:
        soma = soma
        totn = totn
print(f'{totn} numeros a soma foi {soma}')
