"""
Continuação kwargs3.py...
"""

# Entenda porquê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de Parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **Kwargs):
    return [a, b, args, instrutor, Kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

# Função com a ordem errada de Parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **Kwargs):
    return [a, b, args, instrutor, Kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
"""
a = 1
b = 2
args = (0)
instrutor = 3
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]}, {kwargs["sobrenome"]}'

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3) TypeError
# soma_multiplos_numeros(**dicionario)
