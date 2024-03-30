'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
 com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def boletim(*notas,sit=False):
  r = {}
  r['total'] = len(notas)
  r['maior'] = max(notas)
  r['menor'] = min(notas)
  r['media'] = sum(notas)/len(notas)
  if sit:
    if r['media'] >= 7:
      r['situacao'] = 'BOA'
    elif r['media'] >= 5:
      r['situacao']= 'RAZOAVEL'
    else:
      r['situacao'] = 'RUIM'
  return r


#programa principal
resp = boletim(5,2,5,8,sit=True)
print(f'dicionario sobre a situacao do aluno {resp}')
