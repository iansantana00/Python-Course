"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html

Collections - > High-performance Container Datetypes

Counter - > Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter 
que é parecido com um dicionário, contendo como chave um elemento da lista passada como parâmetro
e como valor a quantidade de ocorrências desse elemento.
"""

# Realizando o import 

from collections import Counter 

# Exemplo 1 

# Podemos utilizar qualquer iterável, aqui usamos uma lista 
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter 

# Exemplo 1

res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou um chave e contou a quantidade de ocorrências.

# Exemplo 2 

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = """
Hoje é dia de fazer um pião, já desentoquei o robozão
que a quebrada tá a milhão, várias delas

solzão estralando e nóis já tá como, naquele modelo brasileiro
bem brack então passa um pano no visual dos mandrack original
que é o terror da capital, pega os menino no grau vem na bota

aqui ceis não arruma nada , na fuga os mlk dichava
sobe viela, desce escada no toque da multistrada 
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
