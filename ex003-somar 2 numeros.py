'''Crie um programa que leia dois números e mostre a soma entre eles.'''
def somar_numeros(x,y):
    return x + y


n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
print(f'a soma de {n1} e {n2} é {somar_numeros(n1,n2)}')


