"""
Funções com Parâmetros Padrão (Deafault Paramters)

- Funções onde a passagem de parâmetros seja opcional;
"""

# Exemplos de função onde a passagem de parâmetros seja opcional

print('Geek University')
print() 

# Exemplos de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
# print(quadrado()) #TypeError

def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2,3)) # 2 * 2 * 2 = 8
# print(exponencial(3))  # Errado

# Outra forma

def exponencial(numero, potencia=3): # Parâmtro com valor padrão 
    return numero ** potencia # Eleva a potência informada pelo usuário

print(exponencial(2)) # Por padrão eleve ao quadrado
print(exponencial(3))


# Outra forma 
def exponencial(numero=2, potencia=3): # Parâmtro com valor padrão 
    return numero ** potencia # Eleva a potência informada pelo usuário

print(exponencial())

"""
 OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

#  ERRO! 
def teste(num = 2, potencia):
    return num ** potencia

print(teste(6))
"""
# Certo
def teste(potencia, num = 2):
    return num ** potencia

print(teste(6))

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse instrutor'
    return f'Olá {nome}'

print(mostra_informacao()) 
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) # Vai para o nome, pois quando não deixa explícito irá para o 1º Parâmetro
print(mostra_informacao('Ozzy'))  # Vai para o nome
print(mostra_informacao(nome='Stephany'))
