
class MinhaClasse():

    def __str__(self):
        return (
            f'<Instância de {self.__class__.__name__}; endereço: {id(self)}>'
        )


if __name__ == '__main__':
    mc = MinhaClasse()
    print(dir(mc))
    print(mc)


class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Ponto({self.x + 1}, {self.y + 1})'


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = eval(repr(p1))

    print(p1)
    print(p2)
