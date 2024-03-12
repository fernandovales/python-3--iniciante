km = float(input('qual a distancia da viagem? '))
if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50
print('o valor da passagem será R$ {:.2f}'.format(preco))
