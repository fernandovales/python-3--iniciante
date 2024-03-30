'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''
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
