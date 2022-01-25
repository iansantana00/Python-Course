"""
CONTINUAÇÃO... dicionarios3.py
"""

# Remover dados de uma dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso nao encontre o elemeto, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Nesse caso o valor removido não é retornado

