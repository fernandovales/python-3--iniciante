from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'os numeros sorteados foram{n}')
maior = menor = n[0]
for c in range (0,5):
    if n[c] > maior:
        maior = n[c]
    if n[c] < menor:
        menor = n[c]
print(f'maior foi {maior}')
print(f'menor foi {menor}')
print('=-'*30)
#OUTRA MANEIRA
num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('os numeros sorteados foram:',end='')
for c in num :
    print(f'{c}', end=' ')
print(f'\no maior foi {max(num)}')
print(f'o menor valor foi {min(num)}')
