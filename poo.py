"""
Programação Orientada a Objetos - POO

Paradigmas de Programação:
Estruturada, Orientada e Funcional

Python é uma linguagem multiparadigma

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real
para modelos computacionais, representando suas caracteristicas e comportamentos.


- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a Objetos
- Classe -> Modelo do objeto no mundo real sendo representado computacionalmente
    ex: Produto

- Atributo -> Características do objeto
    ex: Nome, Preço, Desconto 

- Metodo -> Comportamento do objeto, ações que ele executa (função)

- Construtor -> método especial utilizado para criar objetos a partir da nossa classe  
    ex: Notebook (objeto ou instância), 3000, 15 por cento de desconto 
"""

numero = 10 # criar uma variavel inteiro

print(numero)
print(type(numero))

nome = 'geek' # criar uma variavel string
print(nome)
print(type(nome))

class Produto: # Classe
    pass

ps4 = Produto() # Construtor
# ps4 -> Objeto
print(ps4)
print(type(ps4)) # foi criado um tipo de dado chamado Produto