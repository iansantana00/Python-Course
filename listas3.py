"""
CONTINUAÇÃO lista2.py
"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = list('1234568 90923')

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345] 
print(lista7)
print(type(lista7)) 

# Podemos facilmente repetir elementos em uma lista 
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista 

# Exemplo 1 

curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2 
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo a lista em um string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca $ entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)