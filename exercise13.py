
lista = []

for x in range(0, 5):
    lista.append(int(input(f'Digite o valor {x}: ')))

print('-' * 18)

print('lista =', lista)

print('-' * 18)

print('Posição do maior valor:', lista.index(max(lista)))
print('Posição do menor valor:', lista.index(min(lista)))
print('O total de elementos da lista:', len(lista))
print('A soma de todos os elementos da lista é:', sum(lista))
