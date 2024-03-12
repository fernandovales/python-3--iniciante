while True:
    n = int(input('quer ver a tabuada de que numero? '))
    if n < 0:
        break
    for cont in range(0, 11):
        print(f'{n} x {cont} = {n * cont}')
    print('-'*20)
print('FIM')
