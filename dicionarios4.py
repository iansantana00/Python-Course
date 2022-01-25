"""
CONTINUAÇÃO... dicionarios4.py
"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Good of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade':1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade':1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
