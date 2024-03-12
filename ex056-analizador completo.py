totidade = 0
maioridade = 0
nomevelho =''
contmenor = 0
media = 0
for c in range (1,5):
    print('{}ª pessoa:'.format(c))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str (input('sexo [f] ou [m]: ')).strip().lower()
    totidade += idade
    if sexo =='m' and idade > maioridade:
        nomevelho = nome
        maioridade = idade
    if sexo == 'f' and idade < 20:
        contmenor += 1
media = totidade / 4
print('media de idade é {:.1f} anos.'.format(media))
print('o homem mais velho chama-se {} com {} anos'.format(nomevelho,maioridade))
print('{} mulheres tem menos de 20 anos.'.format(contmenor))


