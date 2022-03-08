"""
Manipulando Data e Hora 

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime.
"""

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente    

print(datetime.datetime.now()) # 2022-03-07 10:13:14.810726

# datetime.datetime(year, monthm day, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microssegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data e hora

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informa sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/') # separar a string pela barra e converter em lista 

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year) # ano
print(evento.month) # mês
print(evento.day) # dia
print(evento.hour) 
print(evento.minute)
print(evento.second)
print(evento.microsecond)