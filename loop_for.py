"""
Loop for 

Loop -> Estrutura de repetição.
for -> Uma dessas estrututras.

for item in interavel :
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis (Pode ser escrito uma parte de cada vez)

Exemplos de interáveis: 
- String    
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista 

# Exemplo de for 1 (Interando sobre um string)
for letra in nome: 
    print(letra) 
print('------------')

# Exemplo de for 2 (Interando sobre uma lista)
for numero in lista:
    print(numero)
print('------------')
# Exemplo de for 3 (Interando sobre uma range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não 
"""
for numero in range(1, 10):
    print(numero)
print('------------')
"""
Enumerate

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ')...)
"""
for i, v in enumerate(nome): # i -> indice, v -> letra
    print(nome[i])
print('------------')

for _, v in enumerate(nome): # _ descarta algum valor, que no caso é o indice 
    print(v)
print('------------')

for i, v in enumerate(nome):
    print(v)    

for valor in enumerate(nome):
    print(valor) # adicionado o [0] imprime o indice e o [1] imprime a letra


  