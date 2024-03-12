from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                          #pra não precisar do append

for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = randint(0, 1000)                      #alimentando a matriz

for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')              #mostrando a matriz formatando cada elento em 5 especos e centralizado
    print()                                                         #quebrar sempre que terminar as colunas





