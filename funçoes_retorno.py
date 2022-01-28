"""
Funções com retorno

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None.
OBS: Funções Python que retornam valores devem retornar estes valores com a 
palavra reservada return.
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.
"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# Exemplo  

def quadrado_de_7(): 
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')

# Refatorando (melhorar o código) a função para que retorne valor 

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função 
ret = quadrado_de_7()

print(f'Retorno {ret}')

# Sem variável 
print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função (função.py)

def diz_oi():
    return 'Oi, '

alguem = 'Pedro!'

print(diz_oi() + alguem)

# OBS: Sobre a palavra reservada return


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado após o retorno...') # Não será executado 

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferents returns;

def nova_funcao():
    variavel = False
    if variavel: 
        return 4
    elif variavel is None:
        return 3.22
    return 'b'

print(nova_funcao())


def nova_funcao():
    variavel = True
    if variavel: 
        return 4
    elif variavel is None:
        return 3.22
    return 'b'                                                                                                                                                                                                              

print(nova_funcao())


def nova_funcao():
    variavel = None
    if variavel: 
        return 4
    elif variavel is None:
        return 3.22
    return 'b'

print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao() # Desempacotando
print(outra_funcao())