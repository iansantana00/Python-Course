# -*- Coding: utf-8 -*-

q = int(input("Quantos números serão digitados? "))
print("-----------------------------------")

n = 1
m = 0 
d = 0

while n < q + 1:
    x = int(input(f"Digite o {n}° valor: "))
    if x > m:
        m = x  
        n = n + 1
        d = 1
    else: 
        n = n + 1
        d += 1

print("-----------------------------------")
print(f"O maior valor é: {m}", f"e foi digitado {d}x")
