'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
pc = randint(0,10)
#print('tente advinhar o numero que o computador pensou de 0 a 10:')
#usuario = int(input('digite seu palpite: '))
#tentativas = 1
#while usuario != pc :
 #   usuario = int(input('voce errou. digite novamente seu palpite:'))
  #  tentativas += 1
#print('Voce acertou , foram {} tentativas'.format(tentativas))

acertou = False
tentativas = 0
while not acertou:
    usuario = int(input('qual é seu palpite: '))
    tentativas += 1
    if pc == usuario :
        acertou = True
    else:
        if usuario < pc :
            print('MAIS...tente novamente.')
        elif usuario > pc :
            print('MENOS...tente novamente')
print('ACERTOU com {} tentativas'.format(tentativas))



