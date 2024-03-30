'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
contmaior = contmenor = 0

for c in range (1,8,1):
   nas = int(input('digite a {}° data de nascimento: '.format(c)))
   if atual - nas >=21:
       contmaior += 1
   else:
       contmenor += 1
print('{} pessoas são menores de idade e {} são maiores'.format(contmenor,contmaior))




