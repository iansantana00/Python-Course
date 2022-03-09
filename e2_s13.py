numero_vogal = 0

espaço = 0

numero_consoante = 0

contador = 0

escrita = 0

arquivo =  input('Digite o nome do seu arquivo (.txt): ')

with open(arquivo, 'w', encoding='utf-8') as texto:
    while escrita != 'sair':
        escrita = input('Digite: ')
        texto.write(escrita)
        texto.write('\n')
        contador += 1

with open(arquivo, encoding='utf-8') as texto:
    file = texto.read()
    file.split('\n')
    
    for vogal in file:
        if vogal in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 
        'Ú', 'Â', 'â', 'ã', 'Ã', 'Õ', 'õ', 'ô', 'Ô', 'ê', 'Ê'):
            numero_vogal += 1
    
    for consoante in file:
        if consoante in ('Q', 'q', 'W', 'w', 'R', 'r', 'T', 't', 'Y', 'y', 'P', 'p', 'S', 's', 'D', 'F', 'f', 'g',
        'G', 'h', 'H', 'J', 'j', 'K', 'k', 'L', 'l', 'Ç', 'ç', 'Z', 'z', 'X', 'x', 'C', 'c', 'V', 'v',
        'B', 'b', 'N', 'n', 'M', 'm'):
            numero_consoante += 1


print(f'O número de linhas do texto é {contador - 1}')
print(f'O número de vogais é {numero_vogal - 2}')
print(f'O número de consoantes é {numero_consoante - 2}')
