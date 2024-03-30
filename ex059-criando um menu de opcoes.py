'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
op = False
while not op :
    print('''MENU DE OPÇÕES:
    [1] somar
    [2] multiplicação
    [3] maior
    [4] novos numeros
    [5] sair ''')
    opcao = int(input('digite a opcao:'))
    if opcao == 1 :
        print('a soma de {}+{} é {}'.format(n1,n2,(n1+n2)))
    elif opcao == 2:
        print('a multiplicacao de {}x{} é {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else :
            print('{} é igual a {}'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('novo numero 1:'))
        n2 = int(input('novo numero 2:'))
    elif opcao == 5:
        print('saindo do programa....')
        op = True
    else:
        print('opcao invalida.')
print('FIM DO PROGRAMA')








