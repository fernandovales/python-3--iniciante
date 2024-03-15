

frase = str(input('digite uma frase: ')).strip()
print('a frase tem {} letras [A]'.format(frase.lower().count('a')))
print('a letra [A] aparece primeiro na posição {}'.format(frase.lower().find('a')))
print('a letra [A] aparece pela ultima na posição {}'.format(frase.lower().rfind('a')))
