'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
       'treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
res = ' '
while res not in 'Nn':
    while True:
        n = int(input('Digite um numero de 0 a 20:'))
        if 0 <= n <= 20:
            break
        print('tente novamente.',end=' ')
    print(f'voce digitou o numero {num[n]}')
    while res not in 'SN':
        res = str(input('quer continuar[S/N]'))
print('acabou')




