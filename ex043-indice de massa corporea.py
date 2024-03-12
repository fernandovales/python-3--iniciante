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
