"""
class Conta: # Classe

    def __init__(self): # Método __init__
        self.objeto = objeto # atributos

    def funcao(): # Método
"""

import datetime


class Historico:

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self) -> None:
        print(f'data abertura: {self.data_abertura}')
        print('transações: ')
        for t in self.transacoes:
            print('-', t)


class Cliente:

    def __init__(self, nome: str, sobrenome: str, cpf: str) -> str:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.cpf: str = cpf


class Conta:

    def __init__(
        self, titular: str, numero: str, saldo: float, limite: float = 1000.0
    ) -> None:
        print('inicializando uma conta')
        self.titular: str = titular
        self.numero: str = numero
        self.saldo: float = saldo
        self.limite: float = limite
        self.historico = Historico()

    def deposita(self, valor: float) -> None:
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de {valor}')

    def saca(self, valor: float) -> None:
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')

    def extrato(self) -> None:
        print(f'numero: {self.numero} \nsaldo: {self.saldo}')
        self.historico.transacoes.append(
            f'tirou extrato - saldo de {self.saldo}'
        )

    def transfere_para(self, destino: float, valor: float) -> None:
        retirou = self.saca(valor)
        if retirou is False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(
                f'transferencia de {valor} para conta {destino.numero}'
            )
            return True

    def pega_saldo(self) -> None:
        return self._saldo  # atributo protegido um undescore('_')


cliente1 = Cliente('João', 'Oliveira', '111.111.111-11')
cliente2 = Cliente('José', 'Azevedo', '222.222.222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)


conta1.saca(40000)
conta1.extrato()
