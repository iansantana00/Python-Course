"""
CONTINUAÇÃO funçoes_parametros2.py

Funções podem ter n parâmetros de entrada. 
Ou seja, podemos receber como entrada quantos parametros forem necessários.
Eles são separados por vírgulas.
"""

# Exemplos

def soma(a, b): # Parâmetros a e b 
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5)) # Argumentos 2 e 5
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3, 4)) # TypeError - passando argumentos a mais
# print(soma(4)) # TypeError - passando argumentos a menos