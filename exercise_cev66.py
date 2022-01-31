
x = 0
y = 0
z = 0 

while x != 999:
    numero = float(input('Adicione qualquer número: '))
    if numero == 999:
        break
    y += numero
    z += 1     

print('A soma dos números foi', y)
print('A quantidade de números digitados foi', z)