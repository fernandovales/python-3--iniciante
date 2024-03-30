'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

n = int(input('digite um numero inteiro: '))
print('digite a opção de conversao:')
opcao = int(input('''
[1] binario 
[2] octal 
[3] hexadecimal'''))
if opcao == 1:
    print('{} convertido em binario é {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} convertido em binario é {}'.format(n,oct(n)[2]))
elif opcao == 3:
    print('{} convertido em binario é {}'.format(n,hex(n)[2]))
else:
    print('opcao invalida!')
