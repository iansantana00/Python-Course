"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, ações que este objeto pode realizar
no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de Instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado construtor e sua função é construir
o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim) não
é aconselhado. Python possui vários métodos como esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas interna da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em letra minúsculas. Se o nome for completo, o nome terá as palavras separadas por underline.
# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens.
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1 
        self.__limite = limite 
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp # importar criptografia 

class Usuario:

    contador = 0

    @classmethod # recebe a classe
    def conta_usuarios(cls): # cls dá aceso a classe
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod # não recebe 
    def definicao():
        return 'UXR344'
        
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome 
        self.__email = email         # fazer 200000 embaralhamento da senha e o tamanho que sera juntado e criptografado
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
        # executar o pacote passando a string que quer incriptar, e mais 2 parâmetros para definir a força da senha

    # Atributos de Instância públicos
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha): # verificar pela biblioteca e comparar a senha com self.__senha 
            return True
        return False

    # Atributos de Instância privados
    def __gera_usuario(self):
        return self.__email.split('@')[0]
        
"""
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email =  input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirma a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1) # sair do programa e exibir 1 com código de saída

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso errado
"""
user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))
print(Produto.desconto(p1, 40)) # (self, desconto)
# print(Produto.desconto(50)) 

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(Usuario.nome_completo(user1))

print(user2.nome_completo())

# Metodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

# classe.metodo
Usuario.conta_usuarios() # Forma correta (classe)
user.conta_usuarios() # Possível, mas incorreta (Fazer acesso a atributo de instância)

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

# print(user._Usuario.__gera_usuario()) # Acesso de forma ruim...

# Método Estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user.contador)

print(user.definicao())
