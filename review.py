# Sorted

pares = [10, 2, 6, 4, 8, 12, 16, 14]

print(sorted(pares))

print(sorted(pares, reverse=True))

# List Comprehension

print(sorted([numeros / 2 for numeros in pares]))

lista = [4, 9, 5, 7, 6, 2, 1, 3, 0, 8]

print(sorted([numeros for numeros in lista if numeros > 5 ]))

print([numero / numero if numero > 5 else numero * 0 for numero in lista])

print([letra for letra in 'Ian Santana' if letra != 'a'])

print([x == 'par' if x % 2 == 0 else x == 'impar' for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]])  

import math

def area(r):
    return  math.pi * r ** 2 / 2

print(area(4))

circulo = lambda r: math.pi * r ** 2 / 2

print(circulo(4))

def retangulo(l, c):
    return l * c

print(retangulo(5, 4))

s = lambda l, c: l *c 

print(s(5, 4))

