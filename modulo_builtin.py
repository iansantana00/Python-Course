"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
____________________________
| Python | Módulos Builtin |

https://docs.python.org/3/py-modindex.html

Deve-se fazer o import pois os modulos integrados não vem carregados por padrão para não preencher a memória do código.
"""

# Utilizando alias (apelidos) para módulos/funções
import random as pildes # as serve para dar o apelido

print(pildes.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
# != import random (aqui precisa utilizar o random.random())

print(random())

# Utilizando alias (apelidos) para módulos/funções
from random import randint as barba

print(barba(999, 100000))

# Utilizando alias (apelidos) para módulos/funções
from random import randint as barba, random as pildes

print(barba(-1, 99))

print(pildes())

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
# O shuffle não retorna elemento somente embaralha

print(choice('University'))

