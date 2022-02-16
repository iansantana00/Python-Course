"""
Teste de Memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...
"""

# Função usando listas (Gera tudo de vez, menos eficiente)

def lis_fib(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1 listas 449MB (10000)

for n in lis_fib(10):
    print(n)

# Função usando geradores (Gera de um a um, por causa do next, mais eficiente)

def gen_fib(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 geradores 3MB (10000)
for n in gen_fib(10):
    print(n)