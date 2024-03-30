''' Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''
def anterior_sucessor(n):
    ant = n - 1
    suc = n + 1
    return ant, suc


numero = int(input('Digite um número:'))
anterior , sucessor = anterior_sucessor(numero)

print(f'anterior = {anterior}')
print(f'sucessor = {sucessor}')
