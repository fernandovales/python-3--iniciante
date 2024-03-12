def fatorial(n, show = False):
    '''
    -> funcao fatorial para calcular o fatorial de um numero.
    :param n: numero para calcular o fatorial
    :param show: mostrar o calculo
    :return: retorna o  fatorial de n
    '''
    f = 1
    for c in range (n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x ',end='')
            else:
                print(f'=',end=' ')
    return f

n = int(input('digite um numero: '))
print(f'o fatorial de {n}! é: ')
resp = fatorial(n)
print(resp)
help(fatorial)
