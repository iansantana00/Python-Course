"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular - A classe vai encapsular(englobar) os atributos e métodos.

            classe
---------------------------------
/                               /
/      atributos e métodos      /
/_______________________________/

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se 
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
do usuário.
# Exemplo
Quando fazemos uma ligação de um smartphone para outro, os seguintes passos são executados: 
Ligar o smartphone -> clicar no icone do telefone -> digitar o número do outro aparelho no teclado -> executar a chamada
Entretando, é escondido para o usuário o processo de ligar para a operadora do celular, acessar o banco de dados dela
para encontrar o registro de telefone do outro aparelho para conectar a chamada.
"""

"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Testando

conta1 = Conta('Geek', 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 2019
conta1.titular = 'Ian'
conta1.saldo = 790
conta1.limite = 1050

# Com o acesso público pode fazer a leitura e alteração dos dados

print(conta1.__dict__)
# {'numero': 2019, 'titular': 'Ian', 'saldo': 790, 'limite': 1050}

# OBS: Isso pode ser um problema, pois não garante a segurança dos dados por falta de Encapsulamento
"""
# Como Resolver? Refatorando os dados tornado-os privados

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo!')

    def sacar(self, valor):
        if valor > 0: 
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')

        else:
            print('O valor precisa ser positivo!')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

conta1 = Conta('Ian', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Barba', 400.00, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()

# print(conta1.numero) AttributeError: 'Conta' object has no attribute 'numero'
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)

"""
conta1.numero = 2019
conta1.titular = 'Ian'
conta1.saldo = 790
conta1.limite = 1050


conta1.extrato()

# Pode imprimir e alterar o valor, Mas avisa que não deveria fazer o acesso dessa forma

print(conta1._Conta__titular) # Name Mangling

conta1._Conta__titular = 'Angelina'
"""

print(conta1.__dict__)

conta1.depositar(150)
conta1.depositar(-150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)

conta1.sacar(1800)

print(conta1.__dict__)

conta1.sacar(-300)

print(conta1.__dict__)