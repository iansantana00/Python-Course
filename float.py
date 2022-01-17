"""
Tipo Float 

Tipo real, decimal

Casas decimais (1.24)

Vírgula serve para outras coisas
"""

valor = 1, 44 # Usando vírgula muda a classe, gera tupla
print(valor)
print(type(valor))

# Forma correta
valor = 1.4532
print(type(valor))
print(valor)

valor1, valor2 = 1, 44  # valor1 recebe 1 e valor2 recebe 2 (dupla atribuição)  
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Converter float para inteiro 
res = int(valor)
print(res)
print(type(res))
# OBS: Podemos perder presição 

# Podemos trabalhar com números complexos (o i virá j aqui)
print(type (5j))
