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
