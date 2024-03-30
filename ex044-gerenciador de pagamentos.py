'''
 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''


preco = float(input('digite o preco do produto:R$'))
print('''OPÇÕES DE PAGAMENTO:
[1] A vista dinheiro ou cheque
[2] Á vista no cartão
[3] 2x no cartao
[4] 3x ou mais no cartão''')
opcao = int(input('digite o numero da opçao de pagamento: '))
if opcao == 1:
    npreco = preco - (preco*10/100)
    print('com deconto de 10% o produto saira por R${:.2f}'.format(npreco))
elif opcao == 2:
    npreco = preco - (preco*5/100)
    print('com  desconto de 5% o produto saira por R${:.2f}'.format(npreco))
elif opcao == 3:
    print('em 2x o produto saira por R${:.2f}, a parcela será 2xR${}'.format(preco,preco/2))
elif opcao == 4:
    npreco = preco +(preco*20/100)
    nparcela = int(input('digite o numero de parcelas: '))
    if nparcela < 3:
        print('numero minimo de parcela tem que ser 3x')
    else:
        print('o produto saira por R${:.2f}, dividido em {}xR${:.2f}'.format(npreco,nparcela,npreco/nparcela))
else:
    print('opçao invalida.')




