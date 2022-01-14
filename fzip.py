#irá compactar duas lista (concatenando) como se fosse uma lista (quantas listas quiser)
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
for numero, nome in zip (lista1, lista2):
    print (numero, nome)
