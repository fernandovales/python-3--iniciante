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


