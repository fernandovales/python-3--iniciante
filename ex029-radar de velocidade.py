'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.A multa vai custar R$7,00 por cada Km acima do limite.
'''


vel = float(input('Qual a velocidade: '))
if vel > 80.0:
    print('voce foi multado')
    print('a multa sera de {:.2f}R$'.format(( vel - 80.0 ) * 7.0))
else:
    print('parabens! você esta dentro da velocidade permitida')
