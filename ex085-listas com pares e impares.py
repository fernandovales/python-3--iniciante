'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

from random import randint
num = []
temp = []
par = []
impar = []
for c in range (0,7):
    temp.append(randint(1,10))
    if temp[c] % 2 == 0:
        par.append(temp[c])
    else:
        impar.append(temp[c])
num.append(par[:])
num.append(impar[:])
par.sort()
impar.sort()
print(f'a lista completa dos numeros é {num}',end='')
print()
print(f'os numeros pares foram {par}')
print(f'os numeros impares foram {impar}')







