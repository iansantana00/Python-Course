"""
Doctests

Doctests são testes que colocamos no docstring das funções/métodos Python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

Failed example:
    soma(2, 2)
Expected:
    3
Got:
    4
1 items had no tests:
    doctests
**********************************************************************
1 items had failures:
   1 of   1 in doctests.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.

# Erro inesperado...

OBS: Dentro do doctest, o Python não reconhece string com aspas duplas.
Precisa ser aspas simples.

def fala_oi():
    Fala oi

    >>> fala_oi()
    'oi' # Não pode "oi"
    
    return "oi"
"""


def soma(a, b):
    """soma os numeros a e b

    >>> soma(1, 2)
    3

    >>> soma(8, 2)
    10
    """
    return a + b

# Outro exemplo, Aplicando o TDD


def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar('a', 'b', 'c')
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent  call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

# Um último caso estranho...


def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True

# Há casos em que executar o código com o cursor espaçado irá dar error
# Exemplo: Código   | (coursor)
