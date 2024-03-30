'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
metro = float(input('valor em metros [M]: '))
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000
print('{}m corresponde a: '.format(metro))
print('{}km.'.format(km))
print('{}hm.'.format(hm))
print('{}dam.'.format(dam))
print('{}dm.'.format(dm))
print('{}cm.'.format(cm))
print('{}mm.'.format(mm))
