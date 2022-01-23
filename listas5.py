"""
CONTINUAÇÃO lista5.py
"""

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1 
num2 = 2 
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso a os elementos de forma indexeda ou de forma indexeda inversa

#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde ou -1
print(cores[1]) # amarelo ou -2
print(cores[2]) # azul ou -3 
print(cores[3]) # branco ou -4
# OBS: o indice -5 não existe nessa lista (pense na lista como uma roda, o final está ligado ao início)

for cor in cores:
    print(cores)

indice = 0
while indice < len(cores): # len é a quantidade de cores
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42) 

print(lista)

