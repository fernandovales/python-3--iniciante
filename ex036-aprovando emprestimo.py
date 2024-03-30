'''
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
 o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''


casa = float(input('digite o valor da casa:R$ '))
sal = float(input('digite seu salario:R$ '))
ano = int(input('digite quantos anos : '))
prestacao = casa/(ano*12)
print('o valor da prestacao sera {:.2f}'.format(prestacao))
if prestacao <= sal*30/100:
    print('Emprestimo aprovado.')
else:
    print('Emprestimo negado.')
