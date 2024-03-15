'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de
2 metros quadrados.'''

print('=-'*20)
print('CÁLCULO DE ÁREA')
print('=-'*20)
largura = float(input('digite a largura: '))
altura = float(input('digite a altura: '))
area = largura * altura
tinta = area/2
print('serão necessarios {}l de tinta '.format(tinta))
