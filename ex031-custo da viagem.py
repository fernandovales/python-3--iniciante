'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

km = float(input('qual a distancia da viagem? '))
if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50
print('o valor da passagem será R$ {:.2f}'.format(preco))
