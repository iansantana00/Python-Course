"""
POO - Objetos

Objetos -> São instâncias de classe. Ou seja, após o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar 
nos objetos/instâncias de um classe como variáveis do tipo definindo na classe.
"""

class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')
        
class ContaCorrente:

    contador = 12345

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}') # Acessar atributo privado _nomedaclasse__atributo

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

# Instâncias / Objetos
lamp1 = Lampada('branca', 110, 60)
# lamp1 = Lampada() TypeError, não utilizou os argumentos

lamp1.ligar_desligar() # Irá ligar ou desligar a lâmpada, a depender de sua condição inicial

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

nome = 'Ian'
sobrenome = 'Santana'
email = 'iansantana@gmail.com'
senha = 'ian123'

print(user1) # Só mostrará o endereço de memória  

cli1 = Cliente('Ian Santana', ('123.456.789 - 10'))

cc = ContaCorrente(5000, 1000, cli1)
# cc = ContaCorrente() TypeError, não utilizou os argumentos

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz() # A partir do objeto ContaCorrente, faz acesso ao atributo cliente, que vem do obj Cliente
# que possui o metodo diz dentro 