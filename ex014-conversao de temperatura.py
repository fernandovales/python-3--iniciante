'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

cel = float(input('digite a temperatura em celsius: '))
fah = cel * 9/5+32
k = cel + 273
print('a temperatura {}C corresponde a {}F{} '.format(cel,fah))
print('a temperatura {}C corresponde a {}K{}'.format(cel,k))
