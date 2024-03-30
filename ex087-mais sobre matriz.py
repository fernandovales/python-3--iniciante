'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
from random import randint
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c]=randint(0,11)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
soma = 0
for l in range (0,3):
    for c in range (0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
soma3c = 0
for l in range (0,3):
    for c in range (2,3) :
        soma3c += matriz[l][c]

maior = 0
for l in range(1,2):
    for c in range(0,3):
        if matriz[l][c] > maior:
            maior = matriz[l][c]

print(f'a soma dos numeros pares é: {soma}')
print(f'a soma dos valores da 3 coluna é: {soma3c}')
print(f'o maior valor da 2 linha é : {maior}')





