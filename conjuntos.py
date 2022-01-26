"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, faz referência a Teoria do Conjuntos na Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na Matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados; (nos conjuntos há a ordenação própria, diferente da digitada.)
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, 
mas não no importamos com a ordenação deles. Quando não precisamos se preocupar com 
chaves, valores e itens duplicados.

Os conjuntos são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set*) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um dicionário tem apenas valor;*
    """

# Definindo um conjunto:

# Forma 1 

s = set({1, 2, 3, 4, 8, 9, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, 
# o mesmo será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum 

s = {1, 2, 3, 7, 6, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

"""
É importante lembrar que, além de não termos valores duplicados, 
nos conjuntos há a ordenação própria, diferente da digitada.
""" 

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
