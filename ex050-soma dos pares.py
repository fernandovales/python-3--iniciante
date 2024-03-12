s = 0
for c in range (0, 6):
    n = int(input('digite o {}° numero:'.format(c+1)))
    if n % 2 == 0:
        s += n
print('a soma foi {}'.format(s))
