def contador(i, f, s):
    print('=-'*20)
    if s < 0:
        s *= -1
    if s == 0:
        s = 1
    print(f'contado de {i} ate {f} de {s} em {s}')
    cont = i
    if i < f:

        while cont <= f:
            print(f'{cont}',end=' ')
            cont += s
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            cont -= s
    print('FIM!')
    print('=-'*20)


contador(1,10,1)
contador(10,0,2)
print('agora é a sua vez de personalizar a contagem:')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
salto = int(input('salto: '))
contador(inicio,fim,salto)

