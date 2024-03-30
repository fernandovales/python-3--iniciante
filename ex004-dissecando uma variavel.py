'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele'''

texto = (input('digite algo : '))

print(f'Está capitalizado?{texto.istitle()}')
print(f'o tipo primitivo é {(type(texto))}')
print('é numerico',texto.isnumeric())
print('é letra ',texto.isalpha())
print('é letra ou numero: ',texto.isalnum())
print('é decimal :',texto.isdecimal())
print('é tudo maísculo: ',texto.isupper())
print('é tudo minusculo: ',texto.islower())
print('pode ser impresso: ',texto.isprintable())
