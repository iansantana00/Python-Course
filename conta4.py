class Conta:

    def __init__(self, saldo=0.0) -> None:
        self._saldo = saldo

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('saldo não pode ser negatico')
        else:
            self._saldo = saldo


conta = Conta(1000.0)
conta.saldo = -300.0
