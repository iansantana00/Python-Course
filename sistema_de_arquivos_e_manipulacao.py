"""
Sistema de Arquivos - Manipulação


import os 

# Descobrindo se um arquivo ou diretório existe 

# Arquivo 
print(os.path.exists('arquivo.txt')) # False 
print(os.path.exists('frutas.txt')) # True 

# Diretório

# Paths relativos 
print(os.path.exists('geek')) # True    
print(os.path.exists('geek/university')) # True
print(os.path.exists('geek/university/geek3.py')) # True 
print(os.path.exists('outro')) # False

# Paths absolutos 
print(os.path.exists('/home/geek/university')) # False

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Melhor forma 

os.mknod('arquivo-teste4.txt')

os.mknod('/home/geek/university.txt')

# OBS: Se você estiver utilizando no Mac OS, pode haver um error de PermissionError

# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - únicos(um a um) 

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exita, teremos FileExistsError

os.mkdir('/etc/templates')

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

os.mkdir('templates')   

os.mkdir('templates/geek')

os.mkdir('templates/geek/university')

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university/outro')

# OBS: Se já existir todos os arquivos irá dá FileExistsError, menos se adicionar um novo arquivo ao diretório

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomear arquivos e diretórios

# Diretórios
os.rename('geek', 'geek2')

# Arquivo
os.rename('templates/geek/university', 'university2'
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles 
# não vão para a lixeira. Eles somem.

os.remove('geek2') # Não vai para a lixeira 

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileExistsError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios 

os.rmdir('templates42')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError 

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():   
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios 

os.removedirs('templates/geek') 

# Importando a biblioteca send2trash (envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('cesta.txt') # Vai para a lixeira. Pode ser restaurado.

# OBS: Se o arquivo não existir, teremos OSError

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele crinado
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não vai funcionar se você estiver usando o windows.
# Por conta desse sistema de forma diferente com arquivos temporários.  

# Criando um arquivo temporário

with tempfile.TemporaryDirectory() as tmp:
    tmp.Write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever em bits. Por isso, utilizamos b''


# Sem o bloco with
arquivo = tempfile.TemporaryDirectory()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""

import os 
import tempfile

# Trabalhando com arquivos e diretórios temporários 

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()







