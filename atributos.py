"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor;

# OBS: Método construtor: É um método especial utilizado para a construção do objeto

# OBS: self (é um convenção, portanto pode receber outas denominações) é o objeto que está executando o método.

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público. Ou seja, pode ser acessado
em todo o projeto. Caso queiramos demonstar que determinado atributo deve ser tratado como privado, ou seja, que deve
ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo undescore no ínicio
do seu nome.

Isso é conhecido também como Name Mangling.
"""

# Classes com Atributo de Instância Público

class Lampada:

    def __init__(self, voltagem, cor): # Método Consultores (funções dentro de uma classe)
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class Produto:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não irá impedir
# que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)   

# print(user.__senha) # Attribute Error 

# print(dir(user)) # Temos acesso
# print(dir(user._Acesso__senha)) # Temos acesso, mas não deveriamos fazer esse acesso (Name Mangling)

user.mostra_senha() # Fazendo acesso ao atriburo dentro da própria classe 
user.mostra_email()

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email() 

# Atributos de Classe

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Atributos de classe, são atributos que são declarados diretamente na classe, ou seja, 
# fora do construtor. Geralmente já iniciamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus
# próprios valores como é o caso dos atributos de instância, com os atributos de classe todas 
# instâncias terão o mesmo valor para este atributo.

class Produto:

    # Atributo de Classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Número de resgistro do produto 
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe 

print(p1.id)
print(p2.id)

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Note que na classe Produto não exite o atributo peso  

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}') # Não exite o peso

# Deletando Atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)