"""
POO - Polimorfismo

Poli -> Muitas 
Morfis -> Formas

Quando a gente reimplementa um método presente na classe pai em classes filhas estamos realizando
uma sobrescrita de método (Overriding).

O overriding é a melhor representação do polimorfismo.

Polimorfismo no exemplo está presente nos métodos falar. 
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
        # raise tem como finalidade invocar uma Exception no momento oportuno.

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome} fala "wau wau!"')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome} fala "miau!"')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

bruce = Gato('Bruce')
bruce.comer()
bruce.falar()

jambo = Cachorro('Jambo')
jambo.comer()
jambo.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()