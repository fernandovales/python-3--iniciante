km = float(input('digite a quantidade de km percorridos: '))
dia = int(input('digite a quantidade de dias alugados: '))
preco = km * 0.15 + dia * 60
print('o preco a pagar pelo aluguel sera R${:.2f}'.format(preco))
