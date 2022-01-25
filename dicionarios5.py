"""
CONTINUAÇÃO... dicionarios5.py
"""

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Copiando um dicionário para o outro

# Forma 1 - Deep Copy (somente o novo é atualizado)

novo = d.copy() 

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy (todos os dois são alterados)

novo = d 

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')  # (chave, valor)

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

# Limpar o dicionário (zerar dados)

d.clear()

print(d)