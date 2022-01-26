"""
CONTINUAÇÃO... conjuntos3.py
"""

# Métodos Matemáticos de Conjuntos

""" Imagine que temos dois conjuntos:
Um contendo estudantes do Curso de Python e um contendo estudantes do Curso de Java.
"""

estudantes_python = {'Marcos', 'Pedro', 'Julia', 'Gabi', 'Ian', 'Juan'}
estudantes_java = {'Alvaro', 'Havandecio', 'David', 'Julia', 'Ian'}

# Vejam que alguns alunos de Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
# {'Ian', 'Gabi', 'David', 'Julia', 'Marcos', 'Juan', 'Pedro', 'Havandecio', 'Alvaro'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Havandecio', 'David', 'Juan', 'Julia', 'Pedro', 'Alvaro', 'Ian', 'Gabi', 'Marcos'}
print(unicos1)
# OBS: Só mudou a ordem, mas possuem os mesmos elementos

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_java | estudantes_python
print(unicos2)

#OBS: Não dá para fazer a junção somando as variáveis.

# Gerar um conjuntos de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso 

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ouo reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
