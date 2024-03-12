from random import randint
ganha = 0
minhaopcao = ' '
while True:
    n = int(input('Digite um valor: '))
    maquina = randint(0,10)
    while minhaopcao not in 'PI':
        minhaopcao = str(input('Voce que par ou impar[P/I]: ')).strip().upper()[0]
    if (n+maquina) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'voce digitou {n} e a maquina {maquina}, total de {n+maquina},portanto DEU {resultado}')
    if minhaopcao == resultado[0]:
        ganha += 1
        print(f'voce venceu...VAMOS NOVAMENTE')
    else:
        print('YOU LOSE!')
        break
print(f'voce venceu {ganha} vezes.')


