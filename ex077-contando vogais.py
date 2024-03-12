palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar',
            'praticar','trabalhar','mercado','programador','futuro',)
vogais = ('a','e', 'i','o','u')
valores = list(range(4,11))
print(palavras)
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais',end=' ')
    for letra in c:
        if letra.lower() in vogais:
            print(letra,end='-')
if c not in vogais:
            print('zero vogais')
