"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

Import this

A ideia da PEP8 é que possamos escrever códigos Python da forma Pythônica (não quer dizer que de outra maneira esteja errado)

[1] - Utilize Camel Case para nome de Classe;

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis 


class Calculadora: # [1]
    pass

class CalculadoraCientifica: # [1] Quando a palavra tiver dois nomes, usa-se eles juntos e com as inicias maiúsculas 
    pass

def soma(): # [2] nome de função e variável é aconselhado ser com letra minuscula (lower case)
    pass


def soma_dois(): # [2] ao invés de fazer como no [1], aqui se deve usar o underline para separar dois nomes 
    pass
 

numero = 4

numero_impar = 5    

[3] - Utilize 4 espaços para identação! (afastar da margem)


if 'a' in 'banana':
    print ('tem') #4 espaços

[4] - Linhas em Branco 
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports 
- Imports devem ser sempre feitos em linhas separadas;

# Import Errado 
import sys, os

# Import Certo 
import sys
import os 

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e 
# antes de constantes e variáveis globais.

[6] - Espaços em expressões e instruções 

#  Não faça:

funcao ( algo[ 1 ], { outro: 2 } )

# faça:

funcao (algo[1], {outro: 2})

# Não faça: 

algo (1)

# faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
variavel_longa = 5

# Faça:

x = 1
y = 3 
variavel_longa = 5 

[7] - Termine sempre uma instrução com uma nova linha 

print('algo')

"""
import this 
