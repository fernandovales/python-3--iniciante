'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

clas = ('palmeiras','gremio','atletico mineiro','flamengo','botafogo','bragantino',
        'fluminense','atletico paranaense','internacional','fortaleza','são paulo',
        'cuiaba','corinthians','cruzeiro','vasco','bahia','santos','goias','coritiba','america-mg')

print(f'Os 5 primeiros foram {clas[0:5]}')
print(f'Os times rebaixados foram {clas[-4:]}')
print(f'Listagem em ordem: {sorted(clas)}')
print(f'O fortaleza terminou na {clas.index("fortaleza")+1}ª posicao')


