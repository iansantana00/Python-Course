
class Pessoa:

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def cumprimentar(self):
        return f'{self.__nome} diz: "Olá"!'

    def telefone(self):
        return f'O número de telefone de {self.__nome} é {self.__telefone}'


class Cipoense(Pessoa):

    def __init__(self, nome, telefone, endereço):
        super().__init__(nome, telefone)
        self.__endereço = endereço

    def endereço(self):
        return f'{self._Pessoa__nome} mora em Cipó no(a) {self.__endereço}.'

class Ribeirense(Pessoa):
   
    def __init__(self, nome, telefone, endereço):
        super().__init__(nome, telefone)
        self.__endereço = endereço

    def endereço(self):
        return f'{self._Pessoa__nome} mora na Ribeira no(a) {self.__endereço}.'

ian = Cipoense('Ian', '(75) 93435-9921', 'Rua 5 de agosto')

print(ian)
print(ian.cumprimentar())
print(ian.endereço())
print(ian.telefone())

junior = Ribeirense('Junior', '(75) 98452-9823', 'Rua Dom Pedro')

print(junior)
print(junior.cumprimentar())
print(junior.endereço())
print(junior.telefone())

