"""
POO - Propriedades - Properties

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos
a criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por 
getters e setters, na qual o getters retornam (consultam) o valor do atributo e os setteres alteram seu valor.


class Conta: # Classe

    contador = 0 # Atributo de classe

    def __init__(self, titular, saldo, limite): # Atributos de Instância
        # self.__numero = Conta.contador + 1
        self.__titular = titular # Métodos
        self.__saldo = saldo 
        self.__limite = limite
        # Conta.Contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor 

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return 
    
    def set_limite(self, limite):
        self.__limite = limite 

    
conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())
    
soma = conta1._Conta__saldo + conta2._Conta__saldo # Incorreto, não se deve acessar a variável privada fora da classe
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(9999)
print(conta1.__dict__)
"""

class Conta: # Classe

    contador = 0 # Atributo de classe

    def __init__(self, titular, saldo, limite): # Atributos de Instância
        # self.__numero = Conta.contador + 1
        self.__titular = titular # Métodos
        self.__saldo = saldo 
        self.__limite = limite
        # Conta.Contador += 1

    @property # Propriedades do tipo getter
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter # Criar um setter do getter limite 
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor 

    # Criando um property método (que não está no atributo de instância)
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)