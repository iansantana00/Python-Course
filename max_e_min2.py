"""
CONTINUAÇÃO... max_e_min2.py
"""

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Tim

print(min(nomes)) # Arya

# OBS: Organizar por ordem alfabética da primeira letra

print(max(nomes, key=lambda nome: len(nome))) # Ollivander

print(min(nomes, key=lambda nome: len(nome))) # Tim

# Para cada nome da lista de nomes, ordenar pelos de maior tamanho

musicas = [
    {'titulo': 'Toma vapo vapo', 'tocou': 5},
    {'titulo': 'Malvadao 3', 'tocou': 3},
    {'titulo': 'Brota na pose', 'tocou': 2},
    {'titulo': 'Putariazinha', 'tocou': 1}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])    
    
