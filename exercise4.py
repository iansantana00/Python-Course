# -*- Coding: utf-8 -*-

ms = float(input("Digite uma velocidade em m/s: "))

kmh = ms*3.6

print("Essa velocidade em km/h é: ", kmh)

km = float(input("Agora digite uma distância em km: "))

m = km/1.61

print("Essa distância em milhas é: ", m)

t = km/kmh

print(f"O tempo (h) para percorrer a distância de {km} km com a velocidade de {kmh} km/h é: ", t)

