casa = float(input('digite o valor da casa:R$ '))
sal = float(input('digite seu salario:R$ '))
ano = int(input('digite quantos anos : '))
prestacao = casa/(ano*12)
print('o valor da prestacao sera {:.2f}'.format(prestacao))
if prestacao <= sal*30/100:
    print('Emprestimo aprovado.')
else:
    print('Emprestimo negado.')
