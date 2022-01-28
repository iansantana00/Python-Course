"""
Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções; 
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

Quais tipos de dados podemos utilizar comom valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;
""" 

# Exemplos de funções como valores para parâmetros

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Se não for adicionado nenhum terceiro valor de parâmetro, o parâmetro padrão será soma

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Variável local e global com nomes iguais, a local tem preferência.

"""
def diz_oi():
    prof = 'Geek' # Variável Local
    return f'Olá {prof}'   

print(diz_oi())

print(prof) # NameError 

# OBS: Variável local só é conhecida no seu bloco.

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UboundLocalError
    return total

print(incrementa())

# A variável local está sendo utilizada para processamento sem ter sido inicializada)
"""

total = 0

def incrementa():
    global total # Avisar ao Python que queremos utilizar a variável global
    total = total + 1 
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador 
    return dentro()

print(fora())
print(fora())
print(fora())