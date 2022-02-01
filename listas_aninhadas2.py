"""
CONTINUAÇÃO listas_aninhadas2.py
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Interando com loops em uma lista aninhada 
for lista in listas:
    print(lista)
 
for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension

# [[print(numero) for numero in lista] for lista in listas]
# Para cada lista em listas, imprimir cada numero na lista 

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
#               gerou linhas                      colunas
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['' for i in range(1, 4)] for j in range(1, 4)])