meu_dicionario = {"A": "AMEIXA", "B":"BOLA", "C":"CACHORRO"}
print (meu_dicionario["A"]) #digitando a chave A irá retornar o valor atribuido
for chave in meu_dicionario:
    print (meu_dicionario[chave]) #irá retornar todos os valores atribuidos as chaves
for chave in meu_dicionario:
    print (chave + "-" + meu_dicionario[chave]) #irá digitar a chave mais o valor atribuido
for i in meu_dicionario.items(): #irá digitar a chave e seu valor atribuido em ordem
    print (i)
for i in meu_dicionario.values(): #irá digitar o valor atribuido a chave
    print (i)
for i in meu_dicionario.keys():
    print (i)


