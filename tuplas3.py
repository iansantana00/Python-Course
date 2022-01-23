"""
CONTINUAÇÃO tuplas3...
"""

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla) # O número 3 está na tupla?

# Interando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Dicas na utilização de tuplas

# Devemos sempre utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção 

# Exemplo 1 

meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Interar com While
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Jan'))

meses = ('Jan', 'Fev', 'Mar', 'Jun', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')

print(meses.index('Jun'))
print(meses.index('Jun', 5)) # a partir do indice 5

# OBS: Caso o elemento não exista dará erro, ex: print(meses.index('Agosto'))






