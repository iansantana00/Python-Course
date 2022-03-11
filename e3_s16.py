
class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.calcular_area()
        self.calcular_perimetro()
        self.imprimir()

    def calcular_area(self):
        self.__area = self.__lado * self.__lado

    def calcular_perimetro(self):
        self.__perimetro = self.__lado * 4

    def imprimir(self):
        print(f'A área do quadrado é {self.__area}')
        print(f'O perímetro do quadrado é {self.__perimetro}')


l = float(input('Qual o valor do lado do quadrado? '))

Quadrado(l)
