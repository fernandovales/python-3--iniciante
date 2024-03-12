frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(' 0 inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um Palindromo.')
else:
    print('Não é um palindromo.')
