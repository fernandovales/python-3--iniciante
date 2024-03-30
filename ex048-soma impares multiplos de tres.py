'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''

s = 0
val = 0
for c in range (1,501):
    if c % 2 == 1 and c % 3 == 0:
        s+= c
        val+= 1
print('a soma dos {} valores é {}'.format(val,s))
