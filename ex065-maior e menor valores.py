'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''

media = soma = cont = 0
resp = 's'
while resp not in 'Nn':
    num = int(input('digite um numero: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma += num
    cont+= 1
    resp = str(input('quer continuar[s/n]')).strip()[0]
media = soma/cont
print('FIM')
print('voce digitou {} maior foi {}, menor foi {}, a media foi {}'.format(cont,maior,menor,media))



