'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''

altura = float(input('qual a sua altura? '))
peso = float(input('qual seu peso? '))
imc = peso /pow(altura,2)
print('seu IMC é {:.2f}, voce esta na faixa de'.format(imc),end=' ')
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25.0:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40 :
    print('obesidade')
else:
    print('Obesidade mórbida')
