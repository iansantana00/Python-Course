"""
Teste de Velocidade com Expressões Geradoras 
"""

# Revisão das Diferentes formas de se fazer Geradores 

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1) # Generator

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2) # Generation Expression

print(next(ge2))
print(next(ge2))

# Realizando o Teste de Velocidade
import time

# Generator Expression

gen_inicio = time.time() # Calculando o tempo de início
print(sum(num for num in range(100_000_000))) # 100 milhões
gen_tempo = time.time() - gen_inicio # Calculando o tempo de execução do generator 

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100_000_000)])) # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo} segundos')
print(f'List Comprehension levou {list_tempo} segundos  ')
