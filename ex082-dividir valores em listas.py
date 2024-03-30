'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    res = str(input('quer continuar? [S/N]'))
    if res in 'Nn':
        break
print('=-'*30)
par = []
impar =[]
for c in lista:
    if c % 2 == 0 :
        par.append(c)
    else:
        impar.append(c)
print(f'lista completa {lista}')
print(f'lista dos pares  {par}')
print(f'lista dos impares  {impar}')

