"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now() # now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today() # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()
#                                      date/hora agora     +   adicionar 1 dia,             zerar o tempo  
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda - feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

hoje = datetime.datetime.today()

print(hoje)

if aniversario.weekday() == 0: 
    print('Você nasceu numa segunda-feira')
elif aniversario.weekday() == 1: 
    print('Você nasceu numa terça-feira')
elif aniversario.weekday() == 2: 
    print('Você nasceu numa quarta-feira')
elif aniversario.weekday() == 3: 
    print('Você nasceu numa quinta-feira')
elif aniversario.weekday() == 4: 
    print('Você nasceu numa sexta-feira')
elif aniversario.weekday() == 5: 
    print('Você nasceu numa sábado')
elif aniversario.weekday() == 6: 
    print('Você nasceu numa domingo')
    
def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'

# Formatando datas/horas com striftime()  (String Format Time)
# dd/mm/yyy hora:minuto 

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

# python library datetime 

from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))

# strptime (otimizado) != strftime
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual a sua data de nascimento? (dd/mm/yyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora 

almoco = datetime.time(12, 30, 0) 

print(almoco)

"""

import datetime
from re import L
from time import strftime


import timeit

# Marcando tempo de execução do nosso código com timeit 

# Loop for 
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
print(tempo)

# list comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
print(tempo)

# Map 
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100000)
print(tempo)

import timeit, functools

def teste(n):
    soma = 0 
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

# partial irá receber a função e o parâmetro
print(timeit.timeit(functools.partial(teste, 2), number=10000))