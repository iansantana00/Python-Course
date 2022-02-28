"""
Modos de Abertura de Arquivo

r -> Abre para a leitura - padrão
w -> Abre para a escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo. (append)
+ -> Abre para o modo de atualização: Leitura e Escrita 

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado sempre ao final. Não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open
"""

# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de Comando 2.\n')
except FileExistsError:
    print('Arquivo já existe')

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

with open('outro.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.write('No topo do enem!\n')
    arquivo.seek(11)
    arquivo.write('940 é botar quente.\n')
    arquivo.seek(30)
    arquivo.write('Aprovado, exquece!.\n')
