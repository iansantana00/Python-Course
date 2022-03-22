"""
import collections

from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email')

# criar uma class Pessoa, com atributos nome e email

felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))
"""
