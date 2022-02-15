"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste 
curso são módulos Python prontos para serem utilizados.
"""

# Importando uma função específica do nosso módulo
from funçoes_parametros_padrao import quadrado

print('')
print('Função importada específica:')
print(quadrado(1000))

# Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)
import funçoes_parametros3 as fp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fp.lista) 

print(fp.soma_impares(fp.lista))

from map import cidades, c_para_f 

print(list(map(c_para_f, cidades)))


