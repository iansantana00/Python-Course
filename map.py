"""
Map

Com map, fazemos mapeamento de valores para função.

Temos dados iteráveis:

dados: a1, a2, ..., an

Temos uma função:

funcao: f(x)

Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)

"""

import math

def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2) # Utilizar o pi no cálculo através da biblioteca python 

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum 
areas = []
for r in raios:
    areas.append((area(r)))

print(areas) 

# Forma 2 - Map 

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um interável. Retorna um Map Object

areas = map(area, raios)
# A função map pegara o interável e jogará para a função, ou seja, cada raio da lista raios será usado na função

print(areas)
print(type(areas))

print(list(areas)) # Transformar para ser llido em lista em lista 
print(list(areas))
# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

# Forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), 
           ('Tokio', 27), ('Nova Iorque', 28), ('Londres', 22)]
        
print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))