"""
Escrevendo um iterador customizado

Para criar um iterador customizado necessita-se declarar as duas respectivas funções:

def __iter__

def __next__
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1, 6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) StopInteration

for n in Contador(1, 6):
    print(n)

# Contador funcionando como Range

for n in range(1, 6):
    print(n)