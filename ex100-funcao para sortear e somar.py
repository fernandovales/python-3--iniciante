from random import randint


def sorteio (lista):
    for c in range(5):
        lista.append(randint(0,10))
    print(f'os numeros sorteados foram {lista}')

def soma(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'a soma dos pares em  {lista}  foi  {s} ')
num = []
sorteio(num)
soma(num)




