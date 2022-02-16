"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.
"""

arquivo = open('texto.txt')

print(arquivo.read())

print('')
"""
>>> arquivo = open('texto.txt')
>>> arquivo.read()
'Ã‰ o Barba do ombrinho rei delas e do virote top models boca da peste profeta zikador \nPrograma e 
Programa\nCoding and Coding\nEstuda y Estuda'
>>> arquivo.read()
''
>>> arquivo.read()
''
>>> arquivo.read()
''
# Deve-se atualizar o arquivo com arquivo = open('texto.txt') ou usar a função seek
"""

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. 
# Ela recebe um parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0) # Botar o cursor (procurar) na posição 0, ou seja, a do primeiro caractere

print(arquivo.read())

print('')

arquivo.seek(4) 

print(arquivo.read())

print('')

arquivo = open('texto.txt')

# readline() -> Função que lê cada linha do arquivo por vez

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' ')) # Transformar o texto em uma lista separado por espaços

arquivo = open('texto.txt')

# readlines() -> Função que lê todas as linha do arquivo linha por linha

linhas = arquivo.readlines()

print(len(linhas)) # Saber a quantidade de linhas do texto

"""
# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos
fechar essa conexão. Para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;
"""

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed) # False - Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed) # True - Verifica se o arquivo está aberto ou fechado  

# print(arquivo.read)
# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos ValueError
# Por isso é importante verificar se o arquivo está aberto ou fechado.
