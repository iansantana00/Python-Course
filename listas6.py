"""
CONTINUAÇÃO lista5.py
"""

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice de um elemento da lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista dará erro
print(numeros.index(5)) # Retorna o índice do primeiro elemento encontrado 

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) # buscando o valor 5 a partir do indice 1
print(numeros.index(5,2)) # buscando o valor 5 a partir do indice 2
#print(numeros.index(5,4)) # buscando o valor 5 a partir do indice 4 (Gera erro)

# Podemos fazer busca dentro de um rangem, ínicio/fim
print(numeros.index(8, 3, 6)) # Buscar o indice do valor 8, entre os índices 3 a 6
 
# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com o slice de lista como parâmetro de 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[1]) # Pegar o elemento do indice 1 

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # Começa em 0, pega até o índice 2 menos um 
print(lista[:4]) # Começa em 0, pega até o índice 4 menos um 
print(lista[1:3]) # Começa em 1, pega até índice 3 menos um     

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2 
print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2