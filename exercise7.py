# -*- Coding: utf-8 -*-

print("             LOTERIA              ")
print('----------------------------------')
print("Valor do BILHETE: 10R$")
print("Valor do PRÊMIO: 100.000.000R$")
print('-----------------------------------')

i = float(input("Valor dado pelo 1° amigo para compra do bilhete: "))
a = float(input("Valor dado pelo 2° amigo para compra do bilhete: "))
n = float(input("Valor dado pelo 3° amigo para compra do bilhete: "))

print('-----------------------------------')

if i + a + n > 10:
    print("ERRO!")

else:
    print('PARABÉNS, VOCÊS GANHARAM O PRÊMIO!')
    print('-----------------------------------')
    k = 100_000_000/(i + a + n)
    print("O 1° amigo ficou com", k*i, "R$")
    print("O 2° amigo ficou com", k*a, "R$")
    print("O 3° amigo ficou com", k*n, "R$")
    