'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

p1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))

for c in range (1,11):
    print(p1, end=' ')
    p1 = (p1+r)
print('fim')
