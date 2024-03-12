cadastro = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2)/2
    cadastro.append([nome,[n1,n2],med])
    resp = str(input('Quer continuar?[S/N]')).strip()
    if resp in 'Nn':
        break
print(f'{"LISTAGEM DOS ALUNOS":^40}')
print(f'{"N°.":<4}{"NOME":<10}{"MEDIA":>8}')
for n, aluno in enumerate(cadastro):
    print(f'{n:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opc = int(input('Mostar as notas de qual aluno?[999 interrompe]'))
    if opc <= len(cadastro)-1:
            print(f'as notas de {cadastro[opc][0]} sao {cadastro[opc][1]}')''
    if opc == 999:
        print('FINALIZANDO.....')
        break
print('<<<VOLTE SEMPRE!>>>')

