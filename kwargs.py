"""
**kwargs 

Poderíamos chamar este parâmetro de **xis, por exemplo, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.
""" 

# Exemplo 

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verdes', julia='amarelo', fernando='azul', vanessa='branco')

# Exemplo 2 

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items(): # Para cada pessoa(chave) e cor(valor) em cores_favoritas, imprima-os 
        print(f'A cor favorita de {pessoa.title()} é {cor}') 

cores_favoritas(marcos='verdes', julia='amarelo', fernando='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kawargs):
    if 'geek' in kawargs and kawargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kawargs:
        return f"{kawargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

