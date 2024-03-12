n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
m = (n1+n2)/2
print('media = {:.1f}'.format(m))
if m < 5.0:
    print('\033[1;31mAluno reprovado\033[m')
elif m >= 5.0 and m < 7.0:
    print('\033[1;33mAluno de recuperação\033[m')
elif m >= 7.0:
    print('\033[1;32mAluno aprovado!\033[m')
