# -*- Coding: -*-

n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    soma += i
    for num in range(soma - i + 1, soma + 1):
        print(num, end=" ")
    print()

