'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
def calcular_media(n1,n2):
    #media = (n1+ n2) / 2
    return (n1 + n2)/2
    
    
    
nota1 = float(input('nota 1 : '))
nota2 = float(input('nota 2 : '))
print(f'media: {calcular_media(nota1,nota2):.1f}')


