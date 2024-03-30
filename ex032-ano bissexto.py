'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import date
ano = int(input('digite um ano qualquer: digite 0 para ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('ano bissexto')
else:
    print('ano não bissexto')
