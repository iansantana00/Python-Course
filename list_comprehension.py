"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
interável.

# Sintaxe da List Comprehension

[ dado for dado in interável ]
"""

# Exemplos 

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros] 
# Para cada numero na lista de numeros, multiplica numero * 10 e coloca na nova lista 

print(res)

"""
Para entender melhor, dividir expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10 
"""

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

# List comprehension versus loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

# Outros exemplos

# 1 

nome = 'Geek University'

print([letra.upper() for letra in nome]) 

# 2 

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper()) # Primeira letra do nome vai ser substituido pela sua Maiúscula
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3 

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# 0 e listas vazias são falsas em python

print([str(numero) for numero in [1, 2, 3, 4, 5]])