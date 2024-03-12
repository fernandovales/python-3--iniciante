time = list()
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome']=str(input('nome do jogador: '))
    tot = int(input(f'quantas partidas?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'quantos gols na partida {c+1}')))
    jogador['gols']= partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')

for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca= int(input('mostrar dados de qual jogador? (999 para para.)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogados com esse código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  no jogo{i+1} fez {g} gols.')
    print('-='*30)
print('<<VOLTE NUNCA>>')



