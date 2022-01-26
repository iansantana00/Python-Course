"""
CONTINUAÇÃO... conjuntos2.py
"""
# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)

s.add(4)
s.add(4) # Duplicidade não gera erro. Simplismente é ignorado.
print(s)
 
# Remover elementos em um conjunto

# Forma 1  

s.remove(3) # Não é indice! Informamos o valor a ser removido
print(s)
# OBS: Nenhum valor é retornado.

# s.remove(33) 
# OBS: Caso o valor não seja encontrado será gerado um KyeError

# Forma 2

s.discard(1)
print(s)

# s.discard(22)
# OBS: Se o valor não é encontrado, nenhum error é gerado.

s = {1, 2, 3}
print(s)

# Copiando um conjuto para o outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy 

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)
