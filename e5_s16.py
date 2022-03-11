
class Retangulo:

    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self.calcular_area()
        self.calcular_perimetro()
        self.imprimir()

    def calcular_area(self):
        self.__area = self.__comprimento * self.__largura

    def calcular_perimetro(self):
        self.__perimetro = self.__comprimento * 2 + self.__largura * 2

    def imprimir(self):
        print(f'A área do Retângulo é {self.__area}')
        print(f'O perímetro do Retângulo é {self.__perimetro}')


c = float(input('Digite o comprimento do Retângulo: '))
l = float(input('Digite a largura do Retângulo: '))

Retangulo(c, l)
