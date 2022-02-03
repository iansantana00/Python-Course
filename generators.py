"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque elas se chamam generators
"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension (se quiser o resultado em forma de lista [True, True, True, True, True, False])
res = [nome[0] == 'C' for nome in nomes]
print(type(res))    

# Generator (melhor performance, ocupa menos recurso e memória)
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from re import X
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(190348320890324))

print(getsizeof(True))

# Gerar um sequencia de  0 * 10, 1 * 10... 1000 * 10 e comparar a memória utilizada

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? Sim!

"""
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
"""