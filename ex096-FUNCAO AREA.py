'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''

def area (l, c):
    a = l * c
    print(f'a area de {l} x {c} é {a}m²')


largura = float(input('largura: '))
comprimento = float(input('comprimento: '))
area(largura, comprimento)
