"""
Filter 

filter() -> Serve para filtrar os dados de uma determinada coleção.
"""

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor 
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função men()
media = statistics.mean(dados) # ou sum(dados) / len(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo 
# uma função e um interável.

res = filter(lambda x: x > media, dados) # lambda irá receber um valor e só irá retornar se ele for acima da média.
print(type(res))
print(list(res))

print(f'Novamente: {list(res)}') 
# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memória.

# Filtrar os dados vazios

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuaela']

print(paises)

res = filter(None, paises) 
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)

print(list(res))

"""
# A diferença entre map() e filter() é:

map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para 
cada elemento do iterável. O map trabalha com vários valores

filter() -> Recebe dois parâmetros, uma função e um iterável e retorna filtrando apenas os elementos
de acordo com a função. O filter trabalha com valores bool (True and False), se determinada 
afirmativa for verdadeira ele filtra senão ele não filtra, ou pode fazer ao contrário
"""

# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'twitter': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'ian', 'twitter': []},
    {'username': 'pedro_12', 'twitter': []},
    {'username': 'alvarooo', 'twitter': ['Eu adoro gatos']},
    {'username': 'juan', 'twitter': []},
    {'username': 'victor124', 'twitter': ['Eu vou sair hoje', 'Bora tomar uma']},
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1

inativos = list(filter(lambda usuario: len(usuario['twitter']) == 0, usuarios))
print(inativos)
# Forma 2

inativos = list(filter(lambda usuario: not usuario['twitter'], usuarios))

print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
#                                                       filtar nomes com menos de 5 elementos ['Ana']
# ['Ana'] será passado para map, onde o primeiro parametro vai ser 'Sua instrut..', o segundo é 'Ana'
     
print(lista)