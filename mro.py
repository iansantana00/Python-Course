"""
POO - MRO - METHOD Resolution Order

Resolução da ordem de métodos é a ordem de execução dos métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

>>> from mro import Pinguim
Eu sou Tux do mar!
>>> Pinguim.__mro__
(<class 'mro.Pinguim'>, <class 'mro.Aquatico'>, <class 'mro.Terrestre'>, <class 'mro.Animal'>, <class 'object'>)
# ORDEM DE RESOLUÇÃO DE MÉTODOS

help(Pinguim)
Method resolution order:
 |      Pinguim
 |      Aquatico
 |      Terrestre
 |      Animal
 |      builtins.object
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

    
class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return  f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Aquatico, Terrestre): # Alterando a ordem de herança, irá mudar a execução do código

    def __init__(self, nome):
        super().__init__(nome)

# Testando
tux = Pinguim('Tux')
print(tux.cumprimentar()) # ???? Eu sou Tux da terra!/Eu sou Tux do mar! Method Resolution Order - MRO

"""
class Pinguim(Aquatico, Terrestre):
Eu sou Tux do mar!
"""