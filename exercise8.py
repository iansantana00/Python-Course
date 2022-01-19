# -*- Coding: utf-8 -*- 

print("VERIFICADOR DE CONSUMO")
print("-----------------------")
d = float(input("Distância percorrida pelo carro em km: "))
v = float(input("Quantidade de gasolina consumida em l: "))

c = d/v

if c < 8:
    print(f"Consumo de {c}km/l, VENDA O CARRO!")
elif c > 8 and c < 14:
    print(f"Consumo de {c}km/l, ECONÔMICO!")
else:
    print(f"Consumo de {c}km/l, SUPER ECONÔMICO!")