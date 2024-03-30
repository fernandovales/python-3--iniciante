''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('digite a quantidade de km percorridos: '))
dia = int(input('digite a quantidade de dias alugados: '))
preco = km * 0.15 + dia * 60
print('o preco a pagar pelo aluguel sera R${:.2f}'.format(preco))
