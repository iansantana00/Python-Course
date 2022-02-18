
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

dez = 0

for l in range(0, 4):
    for c in range(0, 4):
        try:
            matriz[l][c] = float(input(f'Digite o valor [{l}][{c}] da matriz: '))
            if matriz[[l][c]] > 10: 
                dez += 1 
        except ValueError:
            print('Valor incorreto!')

print('')

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()

if dez == 0:
    print('Não há valores maiores que 10.')
else:   
    print(f'Existem {dez} valores maiores que 10.')
