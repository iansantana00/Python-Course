"""
Entendendo Iterators e Iterables

Iterator -> 
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""

nome = 'Geek' # É um iterable, mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6] # É um iterable, mas não é um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

# Se o número de next for maior que o número do elemento, irá dá error, 
# pois o next irá passar para o próximo elemento que não existe

print('')

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

print('')

nome = 'Geek'

for letra in nome:
    print(f'{letra}')

# Evitar da error StopIteration, por o loop for para quando acaba os elementos 