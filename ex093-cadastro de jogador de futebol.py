cadastro = dict()
cadastro['nome']= str(input('nome do jogador: '))
partidas = int(input(f'quantas partidas {cadastro["nome"]} jogou? '))
temp = []
for c in range (0,partidas):
    temp.append(int(input(f'quantos gol na partida {c}: ')))
print('=-'*30)
cadastro['gols'] = temp[:]
cadastro['total'] = sum(cadastro['gols'])
print(cadastro)
print('=-'*30)
for k, v in cadastro.items():
    print(f'- O campo {k} tem {v}.')
print('=-'*30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for c in range (0, partidas):
    print(f'na partida {c} fez {temp[c]}')
print(f'foi o artilheiro do time com {cadastro["total"]} gols')
