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
