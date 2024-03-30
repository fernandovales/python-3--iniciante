'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.
'''

sal = float(input('digite seu salario  atual: '))
if sal > 1250:
    nsal = sal + (sal * 10/100) # calculando o novo salario já com a porcentagem de aumento
else:
    nsal = sal + (sal * 15/100)
print('voce recebeu um aumento de R${} e seu novo salario será R${}'.format((nsal-sal),nsal))
