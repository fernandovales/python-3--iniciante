def ajuda(com):
  help(com)


#programa principal
while True:
  comando = str(input('digite o comando para receber ajuda: '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
print('Já acabou jéssica?!')
