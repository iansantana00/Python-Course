"""
Tipo string

string(str) é sempre que estiver entre aspas simples, duplas, triplas
"""
# -*- Coding: utf-8 -*-

nome = "Geek University"
print(nome)
print(type(nome))

nome = "Gina's Bar" # OU 'Gina's Bar' 
print(nome)
print(type(nome))

nome = "Angelina \nJolie" # \n pula uma linha 
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome)) 
print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em uma lista de strings 

# [0,   1,   2,   3,   4,   5,   6,    7,   8,   9,   10,  11,  12,  13,  14]
# ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']
nome = "Geek University"
print(nome[0:4]) # Escrever do G ao Espaço (slice de string)

print(nome[5:15]) 

# ['Geek', 'University'] # Virou uma lista de dois elementos
# [0,         1]
print(nome.split()[0]) # Escrever a lista 0

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta 
"""
print(nome[::-1]) # Inversão da string pythônico

print(nome.replace('e','i')) # Trocar o 'e' pelo 'i'

print(type(nome))

nome = 'ana'
print(nome[::-1])
