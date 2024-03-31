'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
def fazer_operacoes(n):
    d = 2 * n
    t = 3 * n
    r = n ** (1/2)
    return d, t, r


numero = int(input('digite um numero: '))
dobro, triplo ,raizq = fazer_operacoes(numero)
print(f'o dobro de {numero} é {dobro} ')
print(f'o triplo de {numero} é {triplo} ')
print(f'a raiz quadrada de {numero} é {raizq} ')


