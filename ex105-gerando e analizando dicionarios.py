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
