"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas 
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores).
"""

import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'NOVO', '220V', 2340)}])

print(type(ret))

print(ret)

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix) # encode coloca dados
    arquivo.write(ret)

# Lendo o arquivo json/pickle

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo) # decode decodifica dados
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)