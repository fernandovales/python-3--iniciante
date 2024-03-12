sexo = str(input('digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    print('opcao invalida.')
    sexo = str(input('digite novamente o sexo: ')).strip().upper()[0]
print('opcao valida.')


