# -*- Coding: uft-8 -*- 
# Concatenção é a junção de duas variáveis 
a = "Ian"
b = " Santana"

concatenar = a + b + '\n' # '\n' promove a quebra de linhas toda vez que digitar (concatenar)
print (concatenar)
tamanho = len (concatenar) 
#Tamanho do espaço ocupado pela concatenção (utiliza-se len) 
print ('O nome ocupa ',tamanho, ' espaços')
print ('A primeira letra do nome é ', (a[0])) 
#Posição de determinada letra ou valor (utiliza-se a[]), o espaço em branco não é lido
print ('O primeiro nome é ', a[0:3])
print ('Nome todo minúsculo', concatenar.lower())
print ('Nome todo maiúsculo', concatenar.upper())

