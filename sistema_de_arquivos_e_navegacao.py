"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os.

os -> Operating System - Sistema Operacional
"""

# Fazer o import 
import os 

# getcwd() -> pega o current work directory - diretório de trabalho corrente 
# Retorna o path (caminho) absoluto 
print(os.getcwd()) # C:\Users\iansa\Documents\PythonCourse2
 
# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd()) # C:\Users\iansa\Documents

os.chdir('..')

print(os.getcwd()) # C:\Users\iansa

os.chdir('..')

print(os.getcwd()) # C:\Users

os.chdir('..')

print(os.getcwd()) # C:\

os.chdir('..')

print(os.getcwd()) # C:\


# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/geek/')) # True, is abs = é absoluto

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\geek'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

