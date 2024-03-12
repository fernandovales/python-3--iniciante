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
