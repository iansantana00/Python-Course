"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho
para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou entao teremos o erro 
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Modo de Leitura. r -> read() -> Ler
"""

# Exemplo

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

ret = arquivo.read()

print(type(ret))

print(ret) # Essa forma de leitura com variável irá pegar o texto do arquivo e transformar em string para ser lido

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. 
# Esse cursor funciona como o cursor quando estamos escrevendo. Ou seja, o cursor ler de onde ele ta parado para o sentido 
# da direita. Quando utilizamos a função read(), o cursor vai para o final do texto, lendo todo o conteudo do arquivo 
# e não podendo ser relido com a rescrita do código.

print(arquivo.read()) # Esse print é inútil 

arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo

print(arquivo.read(10)) # Ler os 10 primeiros

# Irá parar no décimo caractere, e se botar para ler de novo, continuará desse

print('')

print(arquivo.read())
 