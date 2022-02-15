"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos em Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.
"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado).

import random 

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

"""
# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
dentro do módulo ficaram disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.
"""

print(random.random())

"""
Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas
uma função dentro do módulo random.
"""

# Forma 2 - Importando uma função específica do módulo (Forma recomendada)
from random import random, shuffle

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

print('') 

# uniform() -> Gerar um valor real pseudo-aleatório entre os valores estabelecidos.
from random import uniform

for n in range(10):
    print(uniform(5, 10)) # Gerar um valor de 5 a 10, na qual o 10 não é incluído

print('')

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=' ') # Começa em 1 e vai até 60

print('\n')

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# Shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas) 

shuffle(cartas) # Embaralhar cartas 

print(cartas.pop()) # Selecionar uma carta e tirá-lá do baralho

