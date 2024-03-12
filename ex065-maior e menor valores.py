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



