# CONTINUAÇÃO sistema_de_arquivos_e_navegacao.py

import os 

# '/home/geek/workspace/sistema'

print(os.getcwd()) # /mnt/c/Users/iansa/Documents/PythonCourse2

res = os.path.join(os.getcwd(), 'geek', 'university') #C:\Users\iansa\Documents\PythonCourse2

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o 
# diretório que será juntado ao atual. 

# Podemos listar os arquivos e os diretórios com o listdir()

print(os.listdir())
print(len(os.listdir()))

# Podemos listar os arquivos e os diretórios com mais detalhes com scandir()

print(os.scandir('C:\\'))
print(list(os.scandir('C:\\')))

arquivos = list(os.scandir())
 
print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].inode()) # ?? identificação na árvore de diretórios
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link sombólico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # ???

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrirmos o arquivo.

# scanner.close() 