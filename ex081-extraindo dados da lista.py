lista = []
while True:
    lista.append(int(input('digite um numero:')))
    res = ' '
    while res not in 'SN':
       res = str(input('Quer continuar? [S/N]')).strip().upper()
    if res =='N':
        break
print(f'os numeros digitados foram {lista}')
print(f'foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'a lista em ordem decrescente é {lista}')
print('numero 5 esta na lista na posiçao ' if 5 in lista else 'o numero 5 nao esta ma lista. ',end='')
if 5 in lista:#se o 5 estiver na lista
    for p, c in enumerate(lista):                                                                       #varrer toda a lista pegando posicao e o elemento
        if c == 5:                                                                                      #quando achar o elemento 5
            print(p)                                                                                    #mostrar posição na tela


