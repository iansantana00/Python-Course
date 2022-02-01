"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4) # 1, 2, 3, 4

Se quisermos criar um set (conjunto)   

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{chave: valor for valor in interavel} dict comprehension
[valor for valor in iteravel] list comprehension
"""

# Exemplos

from re import M


numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
# items transforma o dict em lista com tuplas

print(quadrado)

# Transformar lista em dict

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# RELEMBRANDO: No dict não há repetição de chave 

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
# i começa em 0, chaves[a]: valores[1] 

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]
 
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
# A chave sera os numeros, o valor vai ser par ou impar dependendo do numero 

print(res)