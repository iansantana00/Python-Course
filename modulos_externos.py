"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permirtir impressão de textos coloridos no terminal.

# Instalando um Módulo:

pip install nome-do-modulo
"""

# Utilizando o Pacote instalado

from colorama import init, Fore

init()

print(Fore.LIGHTCYAN_EX + 'Ian Santana')

import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)