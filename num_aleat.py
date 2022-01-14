import random #importar valores aleatórios
numero = random.randint (0, 10) #escolher números aleatórios entre 0 e 10
print (numero)

random.seed (1) #escolher sempre um numero (no caso o correspondente a 1) entre os aleatorios
numero = random.randint (2, 5)
print (numero)

lista = [7, 21, 12]
numero = random.choice (lista) #escolher um dos numeros da lista aleatoriamente
print (numero)


