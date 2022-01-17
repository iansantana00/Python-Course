"""
Tipo Booleano 

Álgebra Booleana, criada por George Boole 

2 constantes, Verdadeiro ou Falso 

True -> Verdadeiro
False -> Falso

true e false (lower case é errado)
"""
ativo = False
print(ativo)

# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, e vice-versa.
"""
print(not ativo)

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro devem ser verdadeiros.
"""
logado = True
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.
"""
print(ativo or logado)

print(not 3>5) 

print(7>=3 or 2>5) 

print(7>3 and 5==3+2)


