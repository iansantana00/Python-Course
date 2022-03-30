
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor
        if valor <= 0:
            return 'Não foi possível depositar'

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
        if valor <= 0:
            return 'Não foi possível sacar'

    def extrato(self):
        print(f'numero: {self._numero} \nsaldo: {self._saldo} ')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou is False:
            return False
        else:
            destino.deposita(valor)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def __self__(self):
        return(
            f'Dados da Conta: \nNumero: {self._numero}'
            f'\nTitular: {self._titular} \nSaldo: {self._saldo}'
            f'\nLimite: {self._limite}'
        )


class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2


class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def deposita(self, valor):
        self._saldo += valor - 0.10


"""
if __name__ == '__main__':
    conta = Conta('123-4', 'João', 1200.0, 1000.0)
    conta2 = Conta('123-5', 'Ian', 250.0, 700.0)
    print(conta._titular)
    conta.saca(100)
    print(conta.__dict__)
    conta.deposita(120)
    print(conta.__dict__)
    conta.transfere_para(conta2, 200)
    conta.extrato()
    conta2.extrato()
"""

if __name__ == '__main__':
    conta1 = Conta('123-4', 'Joao', 1000.0, 5000.0)
    conta_corrente1 = ContaCorrente('123-5', 'Jose', 1000.0, 5000.0)
    conta_poupanca1 = ContaPoupanca('123-6', 'Maria', 1000.0, 5000.0)

    conta1.atualiza(0.01)
    conta_poupanca1.atualiza(0.01)
    conta_corrente1.atualiza(0.01)

    print(conta_corrente1._saldo)
    print(conta_poupanca1._saldo)
    print(conta1._saldo)

    print(conta1)
