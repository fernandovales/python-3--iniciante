
def mostrar_mensagem(msg,padrao='m'):
    if padrao == 'm':
        msg = msg.lower()
    else:
        msg = msg.upper()
    return msg


mensagem = (input('digite uma mensagem: '))
info = mostrar_mensagem(mensagem)
print(info)
    
    




