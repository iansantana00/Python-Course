# -*- Coding: uft-8 -*-
a = 2
b = 0
try:
    print (a/b) #Não se pode dividir um número por 0, irá dar erro no programa, então utiliza-se try e except
except:         #para que o programa não trave e continue as outras operações
    print ("Não é permitido divisão por 0")
print (a/a)