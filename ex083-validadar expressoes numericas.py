'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

lista = (str(input('digite a expressão: ')))
print(lista)
if lista.count('(') == lista.count(')'):
    print('expressão matematica É VÁLIDA.')
else:
    print('a expressÃo matematica NÃO É VÁLIDA.')
