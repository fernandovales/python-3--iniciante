'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

boletim = { }
boletim['nome'] = str(input('nome do aluno: '))
boletim['media'] = float(input(f'media do {boletim["nome"]}: '))

if boletim['media'] >= 7:
    boletim['situacao']= 'aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situacao']= 'recuperação'
else:
    boletim['situacao'] = 'reprovado'

for k, v in boletim.items():
    print(f'- {k} :{v}')

print(boletim)


