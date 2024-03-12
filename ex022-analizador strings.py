nome = str(input('digite seu nome completo: '))
#nome = 'Francisco Fernando Vale'
print('maíscula: ', nome.upper())
print('minuscula: ',nome.lower())
#print('qntos caracteres: ',len(nome))
#print('qntos espaços: ',nome.count(' '))
qcarc = int(len(nome))
qesp = int(nome.count(' '))
#print('total de caractere s/ espaco : {}'.format(qcarc-qesp))
print('qnde de letras sem espaços:{} '.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('qntde de letras do primeiro nome: ',len(dividido[0]))


