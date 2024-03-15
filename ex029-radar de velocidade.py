


vel = float(input('Qual a velocidade: '))
if vel > 80.0:
    print('voce foi multado')
    print('a multa sera de {:.2f}R$'.format(( vel - 80.0 ) * 7.0))
else:
    print('parabens! você esta dentro da velocidade permitida')
