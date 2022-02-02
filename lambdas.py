"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplismente lambdas, são funções sem nome, ou seja, funções anônimas.
"""

# Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressões Lambda 
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# .strip() tira o espaços entre as aspas ''. Já o title() deixa somente as inicias maiúsculas
# tudo após o : é o que será retornado 

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY    ', ' jones '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn: <expressao>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradburr', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
           
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# .split(' ') transforma cada elemento em uma lista, ex: ['Isaac', 'Asimov'] -> lista com 2 elementos
# [-1] fará selecionar o último elemento da lista, ou seja, o primeiro em ordem contrária ['Asimov']
# Ou seja, o .sort irá ordenar pela ordem de sobrenome 
# .lower() transformará em minúsculos para não ocorrer de comparar letra minúscula com maiúscula por exemplo 

print(autores)

# Função Quadrática 
# f(x) = a * x ** 2 + b * x + c 

# Definindo a função 

def geradora_funcao_quadratica(a, b, c):
    '''Retorna a função f(x) = a * x ** 2 + b * x + c'''
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5) # Valor de a, b, c

print(teste(0)) # x valendo 0

# Outra forma

#                                a  b  c  x  
print(geradora_funcao_quadratica(3, 0, 1)(2))
