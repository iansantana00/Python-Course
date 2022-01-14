#Função map (pega o elemento da lista e aplica a uma função)
#o primero corresponde a lista, o segundo a função:  map(lista, função)
def dobro(x):
    return x*2
valor = [1, 2, 3, 4, 5]
valor_dobrado = map (dobro, valor)
for v in valor_dobrado:
    print (v)
