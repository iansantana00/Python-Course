"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Refatorar 

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. Mas, not False = True
pares = [numero for numero in numeros if not numero % 2]
# Dessa forma o contrário acontecerá com os impares, pois 1 é True, mas, not True = False

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é true 
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2 

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
# Se o numero for par, multiplique por 2, senão divida por 2