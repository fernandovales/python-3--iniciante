'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente.
'''

def ficha_jogador(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato.")


n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha_jogador(gols=g)
else:
    ficha_jogador(n, g)
