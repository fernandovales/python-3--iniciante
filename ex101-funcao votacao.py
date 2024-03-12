def votacao(ano):
    from datetime import date #importacao de escopo local

    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 18:
        return f'com {idade} anos: NÃO VOTA.'
    elif idade > 65:
       return f'com {idade} anos: VOTO É OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO É OBRIGATÓRIO.'


ano_nascimento = int(input('digite o ano de nascimento: '))
print(votacao(ano_nascimento))
