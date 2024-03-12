time = list()  # Lista vazia para armazenar os dados dos jogadores
jogador = {}   # Dicionário vazio para armazenar os dados de um jogador por vez
partidas = []  # Lista vazia para armazenar o número de gols em cada partida

while True:  # Loop infinito para permitir a entrada de múltiplos jogadores
    jogador.clear()  # Limpa os dados do jogador atual para inserir novos dados
    jogador['nome'] = str(input('nome do jogador: '))  # Pede o nome do jogador e armazena no dicionário 'jogador'
    tot = int(input(f'quantas partidas? '))  # Pergunta quantas partidas foram jogadas
    partidas.clear()  # Limpa a lista de gols das partidas anteriores do jogador

    # Loop para iterar sobre o número de partidas informado pelo usuário
    for c in range(0, tot):
        partidas.append(int(input(f'quantos gols na partida {c+1}? ')))  # Pergunta o número de gols em cada partida e adiciona à lista 'partidas'

    jogador['gols'] = partidas[:]  # Copia a lista 'partidas' para o dicionário 'jogador' sob a chave 'gols'
    jogador['total'] = sum(partidas)  # Calcula o total de gols do jogador e armazena no dicionário 'jogador'
    time.append(jogador.copy())  # Adiciona uma cópia do dicionário 'jogador' à lista 'time' para armazenar os dados de todos os jogadores

    # Loop para verificar se o usuário deseja continuar inserindo dados de jogadores
    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0]  # Pergunta ao usuário se deseja continuar (S para sim, N para não)
        if resp in 'SN':
            break  # Se a resposta for S ou N, sai do loop interno
        print('ERRO! responda apenas S ou N.')  # Se a resposta não for S ou N, exibe uma mensagem de erro

    if resp == 'N':  # Se a resposta for N, sai do loop externo
        break

print('-=' * 30)  # Exibe uma linha de separação após o término do loop

# Exibe o cabeçalho da tabela
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-=' * 30)  # Exibe outra linha de separação

# Loop para imprimir os dados dos jogadores
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 30)  # Exibe outra linha de separação

while True:  # Loop para permitir a busca de dados de um jogador específico
    busca = int(input('mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  no jogo {i+1} fez {g} gols.')
    print('-=' * 30)

print('<<VOLTE NUNCA>>')  # Mensagem de encerramento
