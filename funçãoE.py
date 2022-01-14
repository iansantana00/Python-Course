lista = ['abacate', 'bola', 'cachorro']
for i in range(len(lista)): #range cria vetor e len mede o tamanho
    print (i, lista[i])
#Usando a função enumerate
for i, nome in enumerate(lista):
    print (i, nome)