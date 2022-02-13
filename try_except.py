"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que
o programa pare de funcionar e o usuário receba mensagens de erro inesperadas

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema 
"""

# Exemplo 1 - Tratando um erro genérico

try:
    geek() # geek() irá dar NameError, para o programa continuar a funcionar tem que usar o try/except
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

"""
# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
tratar de forma específica.

# Exemplo 2 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 3 

try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexostente')

# Exemplo 4 
try:
    len(5)
except TypeError as err: 
    print('Você está utilizando uma função inexistente')    
# Tentar capturar uma exceção do tipo TypeError e dê o nome de err
"""
