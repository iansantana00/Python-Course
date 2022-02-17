"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.
"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}') # Nome da função
        print(f'Aqui a documentação: {funcao.__doc__}') # Documentação da função (para que serve)
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print(soma(5, 1))

print('')

print(soma.__name__) # Soma
print(soma.__doc__) # Soma dois números
# OBS: Dados internos da função sendo alterados por causa do decorator (está usando os dados do logar)

print('')

# Resolução do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}') # Nome da função
        print(f'Aqui a documentação: {funcao.__doc__}') # Documentação da função (para que serve)
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print('')

print(soma.__name__) # Soma
print(soma.__doc__) # Soma dois números

print('')

print(help(soma))