"""
Decorators com diferentes assinaturas

"""

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar 

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando

print(saudacao('Angelina!'))

print(ordenar('Picanha', 'Batata Frita'))
# OBS: A função ordenar não pode receber o decorador @gritar, pois este só recebe um parâmetro de entrada
# e a estamos passando dois parâmetros. # TypeError


# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar 

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'
 
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'
     
print(saudacao('Barba'))

print(ordenar('Cuscuz', 'Ovos'))

# Decorar sem parâmetros de entrada

@gritar
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

# Decorador com argumentos

def verifica_primeiro_argumento(valor): # A primeira função serve para o argumento obrigatório
    def interna(funcao): # A segunda função serve para receber a função que irá decorar
        def outra(*args, **kwargs): # A terceira função serve para decorar e receber os valores
            if args and args[0] != valor:
                return f'Valor incorreto! O Primeiro argumento precisa ser {valor}.'
            return funcao(*args, **kwargs)
        return outra
    return interna
  
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando

print(soma_dez(10, 12)) # 22
print(soma_dez(1, 21))  # 22

print(comida_favorita('cuscuz', 'ovo'))
print(comida_favorita('pizza', 'coca'))
print(comida_favorita('coca', 'pizza'))