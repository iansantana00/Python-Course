"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False

print(all((1, 2, 3, 4))) # Todos os números são verdadeiros? True

print(all({})) # iterável vazio: True

print(all('Geek')) # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C'for nome in nomes])) # Todos os elementos começam com 'C'? True 

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
# Gere uma lista para cada numero desse que for par 
# Todos são par, então é True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
# Gere uma lista para cada numero desse que for impar 
# Todos são par, então o conjuto gerado vai ser vazio, que é True

"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver
vazio, retorna False. 
"""

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

print(any([0, False, {}, (), [], 1])) # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))