'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
def conversor_metros(m):
    km = m / 1000
    hm = m / 100
    dam = m / 10
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    return km,hm,dam,dm,cm,mm

metro = float(input('valor em metros [M]: '))
km,hm,dam,dm,cm,mm = conversor_metros(metro)

print('{:.0f}m corresponde a: '.format(metro))
print('{:.0f}km.'.format(km))
print('{:.0f}hm.'.format(hm))
print('{:.0f}dam.'.format(dam))
print('{:.0f}dm.'.format(dm))
print('{:.0f}cm.'.format(cm))
print('{:.0f}mm.'.format(mm))
