def responder_usuario(nome):
    mensagem = (f'seja bem vindo {nome}')
    return mensagem


nome = input('digite seu nome: ')
saudacao = responder_usuario(nome)  
print(saudacao)
