
def busca_caractere(arquivo, caractere):
    
    contador_caractere = 0

    try:
        with open(arquivo, encoding='utf-8') as texto:
            file = texto.read()
            file.split('\n')
            
            for c in file:
                if caractere == c:
                    contador_caractere += 1

        return f'O caractere {caractere} aparece em {texto.name} {contador_caractere} vezes.'

    except FileNotFoundError:
        return 'Error: Arquivo texto não encontrado!'

arquivo_inserido = input('Digite o nome do arquivo no formato "nome.txt": ')
caractere_inserido = input('Digite o caractere a ser buscado no arquivo: ')

print(busca_caractere(arquivo_inserido, caractere_inserido))