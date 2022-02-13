"""
CONTINUAÇÃO try_except ...
"""

# Podemos efetuar de uma vez diversos tratamentos de erros

try:
    print('Geek'[9])
    # len(5)
    # geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as erra2:
    print(f'Deu TypeError: {erra1}')
except:
    print('Deu um erro diferente')

# Executar de outra forma 

# Maneira Correta de Executar

def pega_valor(dicionario, chave):
    return dicionario[chave]
    
dic = {'nome': 'Geek'}
 
print(pega_valor(dic, 'nome'))

"""
# Maneira Errada de Executar

def pega_valor(dicionario, chave)
    return dicionario[chave]

dic = {'nome': 'Geek'}

print(pega_valor(dic, 'game'))
# Não existe a chave 'game', Portanto dará KeyError
"""

# Como Corrigir o Problema acima

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except:
        return None
dic = {'nome': 'Geek'}

print(pega_valor(dic, 'nome'))

