"""
Debugando com pdb

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB - Python Debugger
"""

# OBS: A utilização do print() para debugar código é uma prática ruim.

# Exemplo com Pycharm - Break Point

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos* importar a bibilioteca pdb e então utilizar a função set_trace() 

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

"""
Por quê utilizar este formato?
O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início
do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente
onde vamos debuggar, e ao finalizar já fazemos a remoção.

# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado
como função built-in (integrada) chamada breakpoint()
"""
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)     

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# imprimir 1 (p l), imprimir 3 (p n) ... 

"""
Como os nomes das variaveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
as variáveis, ou seja: p nome_da_variavel

Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""