"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, 
seria o seu valor real sem o sinal.

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, 
e retornar a soma total dos elementos, incluindo o valor inicial.

# OBS: O valor inicial default = 0

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for 
informada retorna o inteiro mais próximo da entrada.
"""
# Só para revisar len

print(len('Geek University'))

print(len({'a': 1, 'b': 2, 'c': 3, 'd':4}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# Exemplos abs

print(abs(-4))
print(abs(-839.12))

# Exemplos sum

print(sum([1, 2, 3, 4, 5], -5))

print(sum((1.78, 12, 1.89, -1.89, -1.78)))

print(sum({'a': 2, 'b': 3, 'c': 2.5, 'd': 7.5}.values()))

# print(sum({'a': 2, 'b': 3, 'c': 2.5, 'd': 7.5})) *TypeError

# Exemplos Round

print(round(10.215))

print(round(9.5))

print(round(9.51))

print(round(10.87233, 2)) # Pega 2 casas decimais

print(round(9.2))

print(round(3.234532, 1)) # Pega 1 casa decimal