"""
CONTINUAÇÃO tuplas4...
"""

# Contando elementos dentro de um tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University') # Converter uma string para tupla
print(escola)   

print(escola.count('e'))

# Slicing

# tupla[inicio:fim:passo]

print(escola[2:5])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.
# Isso porquê são imutáveis

# Copiando uma tuplas para outra 

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
