
print('-'*6, 'BANCO DE DADOS', '-'*6)

class Pessoa:

    def __init__(self, nome, sobrenome, altura):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self._altura = altura


n = input('Qual o seu nome? ')
s = input('Qual o seu sobrenome? ')

try:
    a = int(input('Qual a sua altura em cm? '))
except ValueError:
    a = 'Valor Inválido'

print('-'*28)

pessoa1 = Pessoa(n, s, a)

print(pessoa1.__dict__)

# pessoa1.set.altura(180)
# print(pessoa1.__dict__)