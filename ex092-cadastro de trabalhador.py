'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

cadastro = dict()

cadastro['nome']= str(input('nome do funcionario: '))
ano_nascimento = int(input('ano de nascimento: '))
cadastro['idade']= date.today().year - ano_nascimento
cadastro['ctps'] = int(input('carteira de trabalho. (0 não tem.)'))

if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input('ano da contratação:'))
    cadastro['salario']= float(input('salario'))
    ano_aposentaria = cadastro['ano_contratacao'] + 35
    cadastro['aposentadoria'] = ano_aposentaria - ano_nascimento

for k, v in cadastro.items():
    print(f'{k} tem valor {v}')

