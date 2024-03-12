total = maismil = cont = barato = 0
while True:
    nome = str(input('nome do produto:'))
    preco = float(input('preco do produto:R$'))
    total += preco
    if preco > 1000:
        maismil += 1
    if cont == 0:
        barato = preco
        nomebarato = nome
    if preco < barato:
        barato = preco
        nomebarato = nome
    cont += 1
    resp = ' '
    while resp not in 'SN':
         resp = str(input('deseja continuar?[S/N]:')).strip().upper()[0]
    if resp =='N':
        break
        print('finalizando compras...')
print(f'total gasto : R${total:.2f}')
print(f'total de produtos acima de R$ 1OOO :{maismil}')
print(f'dos {cont} produtos o mais barato foi {nomebarato} custando:R$ {barato}')

