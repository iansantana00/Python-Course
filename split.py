minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r")
print (minha_lista)

busca = minha_string.find("rei")
print ("posição da palavra rei:", busca) 

minha_string = minha_string.replace ("rei","rainha")
minha_string = minha_string.replace ("do","da")
print (minha_string)