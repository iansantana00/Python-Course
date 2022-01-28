"""
CONTINUAÇÃO funç_retor.py
"""

# Vamos criar uma função para jogar uma moeda

from random import random # Importando do pacote random a função random na biblioteca Python 
# random gera números aleatórios sem repetição

def joga_moeda():
    # Gera um número pseudo-randômico (pode existir repetição) entre 0 a 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa' # Não precisa utilizar o else 

print(joga_moeda())
 
 # Criar um pedra-papel-tesoura

def joga_ppt():
    valor = random()
    if valor >= 0.33 and valor < 0.66:
        return 'Pedra'
    elif valor >= 0.66:
        return 'Papel'
    else: # else usado sem necessidade 
        return 'Tesoura'
    
print(joga_ppt())

