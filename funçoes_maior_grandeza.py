"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras
funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de Funções, nós utilizamos isso.

Em Python, as funções são Cidadãs de Primeira Classe, First Class Citizen
"""

# Exemplo - Definindo as Funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as Funções

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, dividir))
print(calcular(4, 3, multiplicar))

# Nested Functions - Funções Aninhadas

# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas)

# Exemplo 

from random import choice 

def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando 

print(cumprimento('Barba do Ombrinho'))
print(cumprimento('Bananpildes'))

# Retornando funções de outras funções  

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'rsrsrsrs', 'kkkkkkkkkkkkkkk', 'hehe'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'kkkkkkkkk', 'rsrsrsrsrs', 'hehe'))
        return f'{pessoa}: {risada}'
    return dando_risada

# Testando

rindo = faz_me_rir_novamente('Barba do Ombrinho Rei delas')

print(rindo())

print(faz_me_rir_novamente('Barba do Ombrinho Rei delas'))
