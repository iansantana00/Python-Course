"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Inteirar sobre dicionários

for chave in receita: # Para cada chave dentro de receita, imprima a chave
    print(chave)

for chave in receita:
    print(receita[chave]) # Para cada chave dentro de receita, imprima os valores

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

for chaves, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
    
# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))