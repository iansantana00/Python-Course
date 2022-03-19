
from typing import List, Set, Dict, Tuple


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

nome: Tuple[str] = 'Geek University'
lista: List[int] = [43, 54, 12, 23]
dicio: Dict[str, int] = {'carlos': 23, 'vini': 54, 'isa': 29}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 32
peso = 87.2

# print(len(idade))

print(__annotations__)
