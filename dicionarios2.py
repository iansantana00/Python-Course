"""
CONTINUAÇÃO... dicionarios.py
"""

"""Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionários, 
como chaves de dicionários. """

# Tuplas, por exemplo, são interessantes para serem usadas com chave de dicionários por serem imutáveis.
localidades = {
    (34.124, 39.625): 'Escritório em Tókio',
    (40.342, 75.321): 'Escritótio em Nova Iorque',
    (37.234, 122.493): 'Escritório em São Paulo'
}   

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 

receita['abr'] = 350 
 
print(receita)

# Forma 2 

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1 

receita['mai'] = 550

print(receita)

# Forma 2 

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma 
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.
