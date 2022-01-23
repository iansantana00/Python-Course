"""
CONTINUAÇÃO lista5.py
"""

# Invertendo valores em uma lista 

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ["Geek", "university"]

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Soma
print(max(lista)) # Máximo 
print(min(lista)) # Mínimo 
print(len(lista)) # Tamanho

# Transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

# Copiando uma lista para outra  (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy() # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, 
# Mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. 
# Isso em Python é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista  [1, 2, 3]
print(lista)

nova = lista # cópia 

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, 
# Mas após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy 

