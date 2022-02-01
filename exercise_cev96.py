
def area(l, c):
    print(f'A área do seu terreno {l}m x {c}m é {l*c}m²')

print('-----CONTROLE DE TERRENO-----')
largura = int(input('Largura (m): '))
comprimeto = int(input('Comprimento (m): '))

print('-'*29)

area(largura, comprimeto)
