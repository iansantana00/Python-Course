class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


conta1 = Conta('123-4', 'João', 1200)
print(conta1.__dict__)
