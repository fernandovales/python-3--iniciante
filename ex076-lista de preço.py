listagem =('faculdade',312,'gasolina',150,'academia',29.99,'personal',60)
print('-'*40)
print(f'{"LISTAGEM DE CONTAS":^40}')
print('-'*40)
for c in range(0,len(listagem),2):
    print(f'{listagem[c]:.<30}RS {listagem[c+1]:>7.2f}')
print('-'*40)


























