"""
Reversed

OBS: Não confunda com função reserve() que estudamos em listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona me qualquer iterável.

Sua função é inverter o iterável chamado list reverse interator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para um Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (set)
print(set(reversed(lista))) # Em set, não definimos a ordem dos elementos

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='') # Escrever a letras na mesma linha  

print('\n') # Pular linha

# Podemos fazer o mesmo sem o uso do for 
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com slice de strings  
print('Geek University'[::-1])

# Podemos também utilizar o reserved() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end=' ')

print('\n')

# Apesar que também já vimos como fazer isso utilzando o próprio range()
for n in range(9, -1, -1):
    print(n, end=' ')



