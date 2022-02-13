"""
CONTINUAÇÃO try_except_else_finally ...
"""

# Exemplo 1

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segunfo número: ')

print(dividir(num1, num2))

# Exemplo 2 - Como otimizar 

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segunfo número: ')

print(dividir(num1, num2))

# Exemplo 3 - Jeito Genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segunfo número: ')

print(dividir(num1, num2))