num = (int(input('digite um numero 1:')),
       int(input('digite um numero 2:')),
        int(input('digite um numero 3:')),
        int(input('digite um numero 4:')))
print(f'voce digitou os numeros {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)}')
else:
    print('o valor 3 nao foi digitado em nenhuma posição')
print('os valores pares digitados foram ',end=' ')
for c in num:
   if c % 2 == 0:
       print(c,end=' ')
