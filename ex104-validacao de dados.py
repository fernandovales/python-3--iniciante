'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
'''

def leitor_int(msg):
  ok = False
  num_validado = 0
  while True:
    numero = str(input(msg))
    if numero.isnumeric():
      num_validado = int(numero)
      ok = True
      print('numero aceito!')
    else:
      print('ERRO. digite um numero inteiro.')
    if ok:
      break
  return num_validado


#programa principal
n = leitor_int('digite um numero: ')
print(f'O numero digitado foi {n}.')
