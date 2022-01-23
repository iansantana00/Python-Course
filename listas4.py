"""
CONTINUAÇÃO lista3.py
"""
from imaplib import Internaldate2tuple


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = list('1234568 90923')

# Interando sobre listas 

# Exemplo 1 (Utilizando for)

soma = 0
for elemento in lista4: # Para cada elemento da lista, imprima o elemento (resumindo)
    print(elemento)
    soma = soma + elemento
print(soma) # Ler todos os elementos e somá-los

# Exemplo 2 (Utilizando while)

carrinho = []
produto = ''

while produto != 'sair': # Até ser digitado 'sair' continue adicionando produtos no carrinho
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho: # Para cada produto adicionado no carrinho, imprima o produto
    print(produto)



