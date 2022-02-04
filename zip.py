"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados 
como entrada em pares.
"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')
# Ou seja, vai pegar o primeiro elemento de cada, depois o sengundo e assim sucessivamente, formando tuplas...

print(zip1)
print(type(zip1))

# Sempre podemos gerar listas, tuplas, sets e dicionários

print(list(zip1))
print(list(zip1)) # Só pode ser usado uma vez, pois depois da primeira será apagada da memória

zip1 = zip(lista1, lista2, 'abc', 'def')
print(tuple(zip1))

zip1 = zip(lista1, 'abc')
print(dict(zip1)) # Dicionário formara pares chave e valor, portanto só dá para juntar 2 elementos no zip

zip1 = zip(lista1, lista2)
print(set(zip1))

lista3 = [6, 7, 8, 9, 10]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
"""
# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso signidica que se estiver
trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos
do menor iterável estiver sido utilizado, não importa a ordem.
"""

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zip2 = zip(tupla, lista, dicionario.values())
print(list(zip2))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados))) # * serve para fazer o desempacotamento dos valores 

# Exemplos mais complexos   

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
# O for irá criar um iterável chamado dado que irá receber o zip em tuplas, dado[0] é a chave e o resto é valor

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))