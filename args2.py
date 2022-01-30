"""
CONTINUAÇÃO args2.py

OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados.
"""

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.123))

# Adiciona a lista como se fosse um elemento

def soma_todos_numeros(*args):
    print(args)
    # return sum(args) # Não dá para somar 

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(numeros)) 


# Desempacotador

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7] # Pode mudar para tupla () ou conjunto {} que irá funcionar

print(soma_todos_numeros(*numeros)) 

""" 
Dá para fazer usando:
num1, num2, num3, num4, num5, num6, num7 = numeros

print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7)) 
"""

