import random
lista = ['pedra', 'papel','tesoura']
pc = random.choice(lista)
print('\033[1;41m{:=^40}\033[m'.format('JOGO-JOKENPÔ'))
usuario = str(input('Digite sua escolha (PEDRA, PAPEL,TESOURA): ')).strip().lower()
if usuario == 'pedra' or usuario == 'papel' or usuario == 'tesoura':
        if pc =='pedra':
            if usuario == 'tesoura':
                res = 'Computador ganhou'
            elif usuario == 'papel':
                res = 'Você venceu'
            elif usuario == 'pedra':
                res = 'Empate'
        elif pc == 'papel':
            if usuario == 'pedra':
                res = 'Computador ganhou'
            elif usuario =='tesoura':
                res = 'Você venceu'
            elif usuario == 'papel':
                res = 'Empate'
        elif pc =='tesoura':
            if usuario =='papel':
                res = 'Computador ganhou'
            elif usuario == 'pedra':
                res = 'Você venceu'
            elif usuario == 'tesoura':
                res = 'Empate'
        print('\033[1;43m{:=^40}\033[m'.format('RESULTADO:'))
        print('O computador escolheu:{}'.format(pc))
        print('Você escolheu:{}'.format(usuario))
        print('\033[1;42mRESULTADO:{}\033[m'.format(res))
else:
    print('OPÇÃO INVALIDA.')




