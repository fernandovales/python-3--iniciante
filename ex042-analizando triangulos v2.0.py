r1 = float(input('digite o comprimento de r1: '))
r2 = float(input('digite o comprimento de r2: '))
r3 = float(input('digite o comprimento de r3: '))
if r1+r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('pode sim formar um triangulo',end=' ')
    if r1 == r2 and r2 == r3:
        print('equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('isosceles')
    else:
        print('escaleno')
else:
    print('não pode formar um triangulo!')
