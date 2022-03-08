"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.9939329
data_final = dd/mm/yyyy 13:34:23.0948484

delta = data_final - data_inical 
"""

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
matricula = datetime.datetime(2022, 3, 16, 0)

# calculando o delta
tempo_para_evento = matricula - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas')

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)