"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados, não alterando 
a lista/tupla/set/dictionary... original 
"""

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)

"""
# Exemplo com Tuplas

numeros = (6, 1, 8, 2) 
print(numeros)
# (8, 1, 2, 6)


print(sorted(numeros)) 
[1, 2, 6, 8]

print(numeros)
(8, 1, 2, 6)
"""

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

print(numeros)

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas 

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'ian', 'tweets': []},
    {'username': 'pedro_12', 'tweets': []},
    {'username': 'alvarooo', 'tweets': ['Eu adoro gatos']},
    {'username': 'juan', 'tweets': []},
    {'username': 'victor124', 'tweets': ['Eu vou sair hoje', 'Bora tomar uma']},
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username'])) 

# Ordenando pelo número de twitter - Menor para o Maior
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']))) 

"""
# Último exemplo 

musicas = [
    {'titulo': 'Toma vapo vapo', 'tocou': 5},
    {'titulo': 'Malvadao 3', 'tocou': 3},
    {'titulo': 'Brota na pose', 'tocou': 2},
    {'titulo': 'Putariazinha', 'tocou': 1}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
[{'titulo': 'Putariazinha', 'tocou': 1}, {'titulo': 'Brota na pose', 'tocou': 2}, 
{'titulo': 'Malvadao 3', 'tocou': 3}, {'titulo': 'Toma vapo vapo', 'tocou': 5}]

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
[{'titulo': 'Toma vapo vapo', 'tocou': 5}, {'titulo': 'Malvadao 3', 'tocou': 3},
 {'titulo': 'Brota na pose', 'tocou': 2}, {'titulo': 'Putariazinha', 'tocou': 1}]
"""