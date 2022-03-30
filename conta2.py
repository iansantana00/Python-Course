
class Conta:

    def __init__(self, titular: str, saldo: float) -> None:
        self._titular: str = titular
        self._saldo: float = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular


conta1 = Conta('João', 200.0)
conta2 = Conta('Jorge', 300.0)
conta3 = Conta('Joana', -100.0)
conta1.get_saldo()
conta2.get_saldo()
conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())
conta3.get_saldo()
