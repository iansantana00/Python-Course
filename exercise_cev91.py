        
from random import randint # Serve para gerar números aleatórios
from time import sleep # Serve para esperar x segundos até aparecer o código
from operator import itemgetter # Escolher se vai ordenar a key (0) ou o value (1)

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = list()

print('Valores sorteados: ')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
# Sorted ordena, integetter vai ordenar por ordem de value (do menor para o maior)
# Mas o reverse vai fazer ser do maior para o menor 

print('-=-'*15)

print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
        print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
        sleep(1)

"""Vamos por partes: 
Olhando a função sorted()
sorted(jogo.items, key, reverse=False) Retorna uma lista sorteada nova dos "itens em jogo".
( key e reverse são opcionais)

key: opcional, neste caso chamou o operador itemgetter.

itemgetter(1) = retorna uma Tupla de valores do item chamado:
(jogador1, resultado)
      0       (1)item chamado

A tupla será dos resultados no dict.jogo, esta será a referencia a ser sorteada  é:
(resultadojogador1, resultadojogador2, ......

reverse = True e para sortear em ordem decrescen
"""