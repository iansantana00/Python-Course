"""
Entendendo o *ags

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo: 
 
*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em um tupla. Então desde já lembre-se que tuplas são imutáveis.     
"""

# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3 


print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(4, 6, 9, 5)) # TypeError

# Entendendo o args 

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2, 3)
soma_todos_numeros(2, 3, 4)
soma_todos_numeros(3, 4, 5, 6)

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))