
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0,], [0, 0, 0, 0]]

maior_valor = 0
linha = 0
coluna = 0

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))

        if matriz[l][c] > maior_valor:
            maior_valor = matriz[l][c]
            linha = l
            coluna = c

        else:
            maior_valor == maior_valor 
            linha == linha
            coluna == coluna

print('-'*32)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^6}]', end='')

    print()

print('-'*32)

print(f'O maior valor foi {maior_valor} e está localizado posição [{linha}, {coluna}]')