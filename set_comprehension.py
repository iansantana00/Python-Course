"""
Set comprehension

lista = []
set = {}
"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Gerar dicionário a partir do set
numeros = {x: x ** 2  for x in range(10)}
print(numeros)

# Para finalizar 

letras = {letra for letra in 'Geek University'}

print(letras)

# Set não repete elementos e são imprimidos aleatoriamente