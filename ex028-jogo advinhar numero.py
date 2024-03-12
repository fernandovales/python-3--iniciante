import random
from time import sleep
print('\033[1;34m{:=^30}\033[m '.format('JOGO: ADVINHE O NUMERO!'))
nome = str(input('Qual seu nome: '))
res = str(input('Seja bem vindo(a) \033[32m{}\033[m!!!\nQuer tentar acertar o numero que estou pensando de 0 a 5? \033[1;32m[sim]\033[m/\033[1;31m[nao]\033[m'.format(nome.lower()))).strip()
if res.lower() == 'sim':
    print('\033[1;34m-'*30)
    print('AGUARDE ,ESTOU SORTEANDO.....')
    print('-'*30)
    sleep(2)
    num_sorteado = random.randint(0,5)
    num_usuario = int(input('\033[mDigite seu palpite: '))
    print('\033[1;34mVERIFICANDO...\033[m')
    sleep(1)
    if num_usuario == num_sorteado:
        print('\033[1;32mPARABÊNS {} você acertou\033[m'.format(nome))
    else:
        print('\033[1;31mPERDEU {}\033[m'.format(nome.lower()))
        print('\033[1;31mvocê disse {} e eu pensei no {}\033[m'.format(num_usuario,num_sorteado))
else:
    print('\033[4;41m{} tá com medo é?\033[m '.format(nome.lower()))

#condição simplificada
#print('USUARIO VENCEU!' if num_usuario == num_sorteado else 'USUARIO PERDEU!')
