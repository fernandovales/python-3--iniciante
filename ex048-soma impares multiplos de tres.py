s = 0
val = 0
for c in range (1,501):
    if c % 2 == 1 and c % 3 == 0:
        s+= c
        val+= 1
print('a soma dos {} valores é {}'.format(val,s))
