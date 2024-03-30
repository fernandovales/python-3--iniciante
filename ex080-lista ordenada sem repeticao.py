'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''

lista = list()
for c in range(0,5):
    n = int(input('digite um numero : '))
    if c == 0 or n > lista[-1]:                     # se o numero for o primeiro ou ultimo da lista de 5 posições
        lista.append(n)
        print('add. no final da fila. ')
    else:
        pos = 0
        while pos < len(lista):                     #varrer o vetor enquanto a pos for menor que o tamanho da lita
            if n <= lista[pos]:                     #se o n é menor ou igual a cada elemento da lista se for:
                lista.insert(pos,n)                 #insere ele naquele posicao
                print(f'add na posicao {pos}.')     #mostrar a posição que ele foi inserido
                break                               #quando for inserido 1 numero quebra o looping subindo pra proxima posicao pos+=1
            pos += 1
print(f'os numeros digitados foram {lista}')



