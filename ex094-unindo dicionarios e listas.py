pessoa = {}
listagem = []
while True:
    pessoa['nome']= str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo:[f/m]')).lower().strip()[0]
        if pessoa['sexo'] in 'fm':
            break
        print('ERRO!digite apenas f ou m.')
    pessoa['idade']= int(input('idade: '))
    listagem.append(pessoa.copy())
    while True:
        resp= str(input('quer continuar? [s/n]')).strip()[0]
        if resp in 'sn':
            break
        print('ERRO! digite apenas s ou n.')
    if resp == 'n':
        break
print(listagem)
qtde_pessoas = len(listagem)
soma_idade = 0
for p in listagem:
    soma_idade += p['idade']
media = soma_idade/qtde_pessoas

print(f'o grupo tem {qtde_pessoas} pessoas')
print(f'a media de idade do grupo é {media:.2f} anos')
print('as mulheres da lista foram:',end='')
for p in listagem:
    if p['sexo'] == 'f':
        print(p['nome'],end=' ')
print()

print('lista de pessoas com idade acima da media:',end='>>')
for p in listagem:
    if p['idade'] > media:
        print(f'nome = {p["nome"]} , sexo = {p["sexo"]} , idade = {p["idade"]}')
