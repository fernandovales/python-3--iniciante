p1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
for c in range (1,11):
    print(p1, end=' ')
    p1 = (p1+r)
print('fim')
