"""
CONTINUAÇÃO... conjuntos.py
"""

# Assim como toda outra coleção Python podemos colocar tipos de dados misturados em sets

s = {1, True, 'b', 34.42, 55}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com sets 

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu.
# Os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, 
# já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Campo Grande', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))


