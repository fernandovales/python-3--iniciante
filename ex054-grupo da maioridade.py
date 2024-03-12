from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for c in range (1,8,1):
   nas = int(input('digite a {}° data de nascimento: '.format(c)))
   if atual - nas >=21:
       contmaior += 1
   else:
       contmenor += 1
print('{} pessoas são menores de idade e {} são maiores'.format(contmenor,contmaior))




