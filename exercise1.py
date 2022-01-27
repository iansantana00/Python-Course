
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Declaração da matriz com o valores que serão substituidos 

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input('Digite o valor para [{l}, {c}]: '))
# Fazer um laço dentro do outro para suprir as linhas e colunas
# Primeiro irá registrar as colunas (0, 0); (1, 0); (2, 0)..., depois as linhas

print('-'*18)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^6}]', end='') 
    print() 
    # o ^6 é para deixar 6 espaços em branco para os números, evitando deformação
    # O end é para deixar um espaço em branco quando for escrever os números na mesma linha
    # O print() quebra a linha, ou seja, ele vai escrever 4 vezes (0, 0); (0, 1), (0, 2)... e depois irá pular uma linha 
