"""
Dicíonarios 

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapa.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}.
"""

print(type({}))

"""
OBS: Sobre dicionários 
    - Chave e valor são separados por dois pontos 'chave: valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados
"""

# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'jp': 'Japao'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', jp='Japao')

print(paises)
print(type(paises))

# Acessando Elementos 

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

# print(paises['arg'])
# OBS: Caso tentarmos fazer acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada 

print(paises.get('br'))
print(paises.get('arg'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = paises.get('arg')

if pais:    
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso encontremos o objeto com a chave informada

pais = paises.get('arg', 'Não encontrado') # Caso não encontre a chave 'arg', coloque 'Não encontrado' no lugar
print(pais)

# Podemos verificar se determinada chave se encontra em um dicionário 

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises: # Evitar error
    russia = paises['ru']
