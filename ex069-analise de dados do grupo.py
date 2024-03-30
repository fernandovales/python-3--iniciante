'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

maior18 = tothomem = totmulher = 0
msg =   'CADASTRO DE PESSOAS'
while True:
    print('-='*20)
    print(f'{msg:-^40}')
    print('-='*20)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo =='M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'total de pessoas maiores de 18 anos :{maior18}')
print(f'total de homnens cadasttrados: {tothomem}')
print(f'total de mulher abaixo de 20 anos: {totmulher}')


