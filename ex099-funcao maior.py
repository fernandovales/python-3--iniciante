from time import sleep
def maior(*num):
    print('analizando os numeros passados...')
    sleep(1)
    maior = 0
    for n in num:
        print(f'{n}',end=' ')
        sleep(0.5)
        if n > maior:
            maior = n
    print(f'foram digitados {len(num)} valores')
    print(f'o maior numero foi {maior}')
    print('=-'*20)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
