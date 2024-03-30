'''
 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''


n = int(input('digite o numero :'))
for c in range (0, 10):
    print('{}x{}= {}'.format(n, c, (n*c)))
print('FIM')
