"""
Mín e Máx

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.
"""

# Exemplos Máx

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(lista)) # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario)) # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values())) # 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max('Geek University'))

print(max(9, 10.43, 4.1293, 5.832, 6))

print(max('a', 'abc', 'ab'))

# Exemplos Mín

lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario)) # a

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values())) # 1

print(min('Geek University')) # O menor é o espaço

print(min('c', 'abd', 'a', 'b'))