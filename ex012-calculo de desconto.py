''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
preco = float(input('digite o preco do produto: '))
desconto = preco * (5 / 100)
print('o preco com desconto fica {}{:.2f}{}'.format(preco-desconto,))
