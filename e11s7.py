
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}][{c}]: '))

diagonal_s = (matriz[2][0], matriz[1][1], matriz[0][2])
soma = sum(diagonal_s)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()

print(f'A soma dos elementos da diagonal secundária é {soma}')
