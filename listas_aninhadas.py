"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (c/java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Mutidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 'b', 3.224, True, 5]
"""

# Exemplos

# elemento    0          1          2
# indice   0, 1, 2    0, 1, 2    0, 1, 2
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
#         |linha 0|  |linha 1|   |linha 2| 
#         c0, c1, c2  c0, c1, c2  c0, c1, c2     

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # Acessar linha 0, coluna 1 (número 2)
print(listas[2][0]) # Acessar número 7
print(listas[2][-2]) # Acessar o 8 de modo não convencional 

