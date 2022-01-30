"""
Documentando funções com Docstrings

print(help(print))

OBS: Podemos ter acesso à documentação de um função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()
"""

def diz_oi():
    """Uma função simpes que retorna a string 'Oi!'"""
    return 'Oi!'

# Acessando a documentação da função

print(diz_oi.__doc__) 

# OU

# print(help(diz_oi)) 

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero'.
    """
print(exponencial.__doc__)
