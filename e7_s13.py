
def troca_vogal(arquivo, vogal):

    try:
        with open(arquivo, 'r', encoding='utf-8') as texto:
            file = texto.read()
            file = file.replace(vogal, '*')

        with open('alterado.txt', 'w') as texto:

            texto.write(file)

    except FileNotFoundError:
        return 'Error: Arquivo texto não encontrado!'


arquivo_inserido = input('Digite o nome do arquivo no formato "nome.txt": ')
vogal_inserida = input('Digite a vogal substituida no arquivo: ')

print(troca_vogal(arquivo_inserido, vogal_inserida))
