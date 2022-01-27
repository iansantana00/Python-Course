
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 5):
        if l == c:
            matriz[l][c] = 1
        
        else:
            matriz[l][c] = 0

for l in range(0, 5):
    for c in range(0, 5):
        print(f'{matriz[l][c]:^6}', end='')
    
    print()