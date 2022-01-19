# -*- Coding: utf-8 -*-

"""
Estruturas Lógicas

Operadores Unitários:
    - not
Operadores Binários:
    - and, or, is 
"""

ativo = True
logado = False

if ativo is True: 
   print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else: 
    print('Bem-vindo usuário!')

# ativo é Falso?
print(ativo is False)

nome = "Geek"
print(nome.isupper()) # O nome está todo maiúsculo?
print(nome.istitle()) # A inicial do nome está maiúscula?
print(nome.lower().islower()) # Converter o nome para minúsculo e depois pergunta se está minúsculo
print(nome is "geek")
