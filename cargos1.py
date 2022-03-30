
class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10 + 1000.0


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

    def autentica(self, senha):
        if self._senha == senha:
            print('acesso permitido')
            return True
        else:
            print('acesso negado')
            return False


funcionario = Funcionario('João', '111.111.111-11', 2000.0)
print(funcionario.__dict__)

gerente1 = Gerente('José', '222.222.222-22', 5000.0, '1234', 0)
print(gerente1.__dict__)

print(gerente1.get_bonificacao())


class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += funcionario.get_bonificacao()
        else:
            print(
                f'instância de {self.__class__.__name__}'
                'não implementa o método get_bonificacao()'
            )

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


if __name__ == '__main__':
    funcionario = Funcionario('João', '111.111.111-11', 2000.0)
    print(f'bonificação funcionário: {funcionario.get_bonificacao()}')

    gerente = Gerente('José', '222.222.222-22', 5000.0, '1234', 0)
    print(f'bonificação gerente: {gerente.get_bonificacao()}')

    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)

    print(f'total: {controle.total_bonificacoes}')
