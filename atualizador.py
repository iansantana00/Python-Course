from banco1 import Conta


class AtualizadorDeContas:

    def __init__(self, numero, titular, saldo, limite, selic, saldo_total=0):
        super().__init__(numero, titular, saldo, limite)
        self._selic = selic
        self._saldo_total = saldo_total

    # propriedades

    def roda(self, conta):
        print(f'Saldo da Conta: {conta._saldo}')
        self._saldo_total += conta.atualiza(self._selic)
        print(f'Saldo Final: {self._saldo_total}')


if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0, 5000.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
