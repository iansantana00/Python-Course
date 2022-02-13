"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.
"""

num = 'um comando inválido!'

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor Incorreto')

print(f'Você digitou {num}')

# Importante declarar uma variável universal, pois se der error com a variável local, não conseguirá ler a var num

# Exemplo - Else

# Else é executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando Finally') # Poderia botar o print no começo sem o finally que daria na mesma

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally geralmente é utilizado para fechar ou desalocar recursos.

"""
# Exemplo mais complexo

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))
# Pode ocorrer error aqui 

num2 = int(input('Informe o segundo número: '))
# Pode ocorrer error aqui

print(dividir(num1, num2))
# Se ocorrer error em num1 ou em num2 ocorrerá error aqui, pois a var não sera criada 

# Se ocorrer error na var deve ser tratado na sua utilização 
# O error deve ser tratado sempre antes do código executado
"""


def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: ')) 

try:    
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

# Tratando error na var

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

